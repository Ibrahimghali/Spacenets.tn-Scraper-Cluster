# Spacenets Scrapy Spider

## Overview

The Spacenets Scrapy Spider is a web scraper designed to extract laptop data from the Spacenets website. This spider collects details such as name, price, operating system, memory, ports, wireless connectivity, warranty, screen size, processor type, hard drive, cache, graphics card, processor details, color, touchscreen, gamer status, graphics card reference, and PC range.

## Features

- Scrapes laptop details from the Spacenets website.
- Handles pagination to scrape multiple pages.
- Follows links to individual laptop pages for detailed information.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/spacenets-spider.git

   cd spacenets-spider

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   pip install -r requirements.txt

Usage
Run the Spider:
scrapy crawl spacespider

Save Output to a File: To save the scraped data to a JSON file, use the following command:
scrapy crawl spacespider -o output.json


Configuration
Modify spacenets/settings.py to configure Scrapy settings such as user agents, download delays, and more.

Contributing
Feel free to open issues or submit pull requests if you find any bugs or want to add new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions, please contact your email.
