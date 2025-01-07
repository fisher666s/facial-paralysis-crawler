import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = ""    # Add facial_paralysis_images url

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was not successful
except requests.exceptions.RequestException as e:
    print("Error fetching the main page:", e)
    exit(1)

soup = BeautifulSoup(response.content, "html.parser")
image_urls = []

for img_tag in soup.find_all("img"):
    img_url = img_tag.get("src")
    if img_url and not img_url.startswith("data:"):  # Skip data URLs
        img_url = urljoin(url, img_url)  # Convert to absolute URL if needed
        image_urls.append(img_url)

if not image_urls:
    print("No images found on the page.")
    exit(0)

save_folder = "facial_paralysis_images"
os.makedirs(save_folder, exist_ok=True)

for img_url in image_urls:
    img_name = os.path.basename(img_url)
    img_path = os.path.join(save_folder, img_name)

    try:
        img_response = requests.get(img_url)
        img_response.raise_for_status()  # Raise an exception if the request was not successful
    except requests.exceptions.RequestException as e:
        print("Error fetching image:", e)
        continue

    with open(img_path, "wb") as img_file:
        img_file.write(img_response.content)
        print(f"Downloaded: {img_name}")

print("All images downloaded successfully.")