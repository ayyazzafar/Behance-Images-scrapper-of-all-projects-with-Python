# Behance Image Scraper

This is a Python-based web scraper that extracts images from the projects of a specified Behance profile.

## Description

The script opens the Behance profile, scrolls through the page to load all projects, opens each project and downloads all images. In case the script is unable to find images with the main CSS selector, it tries to find images with an alternative selector.

## Dependencies

This project is written in Python and uses the following libraries:

- os
- time
- requests
- BeautifulSoup
- selenium

## Installation

To set up the project:

1. Clone this repository to your local machine.
2. Install the required dependencies. Run `pip install -r requirements.txt` in your command prompt.

## Usage

1. Replace the URL in the `main()` function with the URL of the Behance profile you want to scrape images from.
2. Run the script. The images will be saved in folders named after the project titles.

```bash
python main.py
```

## License

This project is licensed under the MIT License.

## Disclaimer

This code is for educational purposes only. Before scraping a website, make sure to understand and respect the website's `robots.txt` file and Terms of Service.
