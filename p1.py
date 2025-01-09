from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time

# Path to your ChromeDriver
driver_path = r"C:\Users\Admin\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# Define the URLs
urls = [
    "https://www.investopedia.com/terms/m/mutualfund.asp",
    "https://www.amfiindia.com/investor-corner/knowledge-center/what-are-mutual-funds-new.html",
    "https://zerodha.com/varsity/chapter/introduction-to-mutual-funds/",
    "https://en.wikipedia.org/wiki/Mutual_fund"
]

# Function to scrape a page using Selenium
def scrape_page(url):
    try:
        driver.get(url)  # Load the webpage
        time.sleep(3)  # Wait for the page to load (adjust as needed)

        # Get the fully rendered page source
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Initialize fields
        overview = ""
        summary = ""
        description = ""
        keywords = ""

        # Extract content based on the webpage structure
        if "investopedia" in url:
            overview = soup.find('p').get_text(strip=True)  # First paragraph
            summary = overview
            description = " ".join([p.get_text(strip=True) for p in soup.find_all('p')[:5]])  # First 5 paragraphs
            keywords = ", ".join([tag.get_text(strip=True) for tag in soup.find_all('a') if tag.get_text(strip=True) not in ['Related Content', 'ADVERTISEMENT']][:10])  # Filter unwanted tags
        
        elif "amfiindia" in url:
            overview = soup.find('h2').get_text(strip=True)  # First heading
            description = " ".join([p.get_text(strip=True) for p in soup.find_all('p')[:5]])  # First 5 paragraphs
            summary = overview
            keywords = ", ".join([tag.get_text(strip=True) for tag in soup.find_all('a') if tag.get_text(strip=True) not in ['Related Links']][:10])  # Filter unwanted links
        
        elif "zerodha" in url:
            overview = soup.find('h1').get_text(strip=True)  # Main heading
            description = " ".join([p.get_text(strip=True) for p in soup.find_all('p')[:5]])  # First 5 paragraphs
            summary = overview
            keywords = ", ".join([tag.get_text(strip=True) for tag in soup.find_all('a') if tag.get_text(strip=True) not in ['Related Content']][:10])  # Filter unwanted tags
        
        elif "wikipedia" in url:
            overview = soup.find('p').get_text(strip=True)  # First paragraph
            description = " ".join([p.get_text(strip=True) for p in soup.find_all('p')[:5]])  # First 5 paragraphs
            summary = overview
            keywords = ", ".join([tag.get_text(strip=True) for tag in soup.find_all('a') if tag.get_text(strip=True) not in ['Related Topics', 'External Links']][:10])  # Filter unwanted links
        
        # Ensure correct encoding
        overview = overview.encode('utf-8').decode('utf-8')
        summary = summary.encode('utf-8').decode('utf-8')
        description = description.encode('utf-8').decode('utf-8')
        keywords = keywords.encode('utf-8').decode('utf-8')

        # Return the data in dictionary format
        return {
            "Overview": overview,
            "Summary": summary,
            "Description": description,
            "Keywords": keywords,
            "Link": url
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Collect data from all URLs
data = []
for url in urls:
    page_data = scrape_page(url)
    if page_data:
        data.append(page_data)

# Close the Selenium WebDriver
driver.quit()

# Save the data to a JSON file
output_file = "mutual_funds_selenium.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Data saved to {output_file}")
