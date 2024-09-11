# Spacenets.tn-Scraper

This project is a web scraper built using the Scrapy framework. It is designed to extract data from the Spacenets.tn website, which sells various electronic products, including air conditioners, laptops, servers, and more. The scraped data is stored in a JSON file and can be further processed for analysis or other uses.

## Project Structure

    Spacenets.tn-Scraper/
    ├── README.md            # Project documentation
    ├── scrapy.cfg           # Scrapy configuration file
    └── spacenets            # Main project directory
        ├── __init__.py      # Initialize the spacenets module
        ├── items.py         # Defines the data structure for scraped items
        ├── middlewares.py   # Custom middlewares (if any)
        ├── output.json      # Output file for storing scraped data in JSON format
        ├── pipelines.py     # Handles the processing of scraped items
        ├── __pycache__/     # Cached files
        ├── settings.py      # Scrapy settings configuration
        └── spiders/         # Directory containing spider definitions
            ├── __init__.py                  # Initialize the spiders module
            ├── item_spider.py               # Spider for extracting item-specific data
            ├── cleaned_data.json            # Cleaned data after post-processing
            └── __pycache__/                 # Cached files for spiders


### Files and Directories

- **README.md**: This file, providing an overview of the project.
- **scrapy.cfg**: Configuration file for the Scrapy project.
- **spacenets**: The main directory containing the Scrapy project modules.
  - **items.py**: Defines the data structure of the items being scraped.
  - **middlewares.py**: Custom middlewares, if any, to process requests or responses.
  - **output.json**: The output file where the scraped data is saved in JSON format.
  - **pipelines.py**: Contains the item pipeline to process and clean the scraped data.
  - **settings.py**: Configuration settings for the Scrapy project.
  - **spiders**: Directory containing all the spider scripts responsible for scraping different parts of the website.
    - **item_spider.py**: Spider that scrapes specific item details like prices, availability, etc.
    - **cleaned_data.json**: Cleaned version of the scraped data.

### How to Use

1. **Clone the Repository**: Clone the project repository to your local machine.

    ```bash
    git clone https://github.com/Ibrahimghali/Spacenets.tn-Scraper.git
    cd Spacenets.tn-Scraper
    ```

2. **Install Dependencies**: Install the necessary dependencies. It's recommended to use a virtual environment.

    ```bash
    pip install scrapy
    ```

3. **Run a Spider**: To start scraping, run a specific spider using the Scrapy command.

    ```bash
    scrapy crawl <spider_name> -o output.json
    ```

    Replace `<spider_name>` with the name of the spider you want to run, such as `item_spider`.

4. **View the Output**: The scraped data will be saved in the `output.json` file in the `spacenets` directory.

### Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License.
