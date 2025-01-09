
# Mutual-Fund-Scraper

## Description
This project automates the process of scraping information about mutual funds from multiple websites using **Selenium** and **BeautifulSoup**. It extracts key content such as overviews, descriptions, summaries, and keywords, and stores this data in a structured JSON file for easy access.

## Features
- Scrapes data from websites like **Investopedia**, **AMFI India**, **Zerodha**, and **Wikipedia**.
- Extracts **Overview**, **Summary**, **Description**, and **Keywords** from the pages.
- Runs the scraper in **headless mode** to avoid opening a browser window.
- Saves the scraped data as a **JSON file** for easy retrieval.

## Technologies Used
- **Selenium**: For automating the browsing and interaction with websites.
- **BeautifulSoup**: For parsing the HTML content and extracting relevant information.
- **Python**: Programming language used for writing the script.
- **JSON**: Format used for storing the scraped data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Mutual-Fund-Scraper.git
    ```

2. Install required dependencies:
    ```bash
    pip install selenium beautifulsoup4
    ```

3. Download **ChromeDriver** for your operating system from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and update the path in the script.

## Usage

1. Run the script to start scraping:
    ```bash
    python mutual_fund_scraper.py
    ```

2. The scraped data will be saved in a file named `mutual_funds_data.json`.

## Output Format
The scraped data is saved in a structured JSON format with the following fields:
- **Overview**: A brief introduction to the topic.
- **Summary**: Key points and highlights.
- **Description**: Detailed explanation of the topic.
- **Keywords**: Relevant keywords extracted from the page.
- **Link**: The URL of the scraped page.

