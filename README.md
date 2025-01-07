# Image Downloader Script

This Python script is designed to download all facial paralysis images from a specified webpage and save them to a local folder. It is particularly useful for scraping images from photo galleries or other image-heavy web pages.

## Features
- Fetches all images from a given URL.
- Skips inline images (e.g., SVGs embedded as data URLs).
- Converts relative image URLs to absolute URLs.
- Saves images to a specified folder on your local machine.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`, `lxml`

You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4 lxml
