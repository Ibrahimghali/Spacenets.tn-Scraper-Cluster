# Spacenets.tn-Scraper

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
Navigate to the Project Directory:

bash

cd spacenets-spider
Create and Activate a Virtual Environment (optional but recommended):

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Spider:

bash
Copy code
scrapy crawl spacespider
Save Output to a File:

To save the scraped data to a JSON file, use the following command:

bash
Copy code
scrapy crawl spacespider -o output.json

spacenets/spiders/spacespider.py: Contains the main spider code.
spacenets/items.py: Defines the data structure for the scraped items.
requirements.txt: Lists the Python packages required for the project.
Configuration
Modify spacenets/settings.py to configure Scrapy settings such as user agents, download delays, and more.

Contributing
Feel free to open issues or submit pull requests if you find any bugs or want to add new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions, please contact your email.

csharp
Copy code

You can copy the contents of this file into your project’s Python and Markdown files as needed.