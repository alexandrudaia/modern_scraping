#pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def get_font_size_from_content_area(url):
    # Set up the WebDriver
 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Load the webpage
        driver.get(url)

        # Try to identify the main content area using multiple possible selectors
        content_selectors = ['main', 'article', 'div#main-content', 'div.content', 'section']
        content_area = None

        for selector in content_selectors:
            try:
                content_area = driver.find_element(By.CSS_SELECTOR, selector)
                break
            except NoSuchElementException:
                continue

        if not content_area:
            # As a fallback, look for the largest paragraph or div block
            paragraphs = driver.find_elements(By.TAG_NAME, 'p')
            divs = driver.find_elements(By.TAG_NAME, 'div')
            all_blocks = paragraphs + divs
            content_area = max(all_blocks, key=lambda x: len(x.text), default=None)

        if content_area:
            # Get the computed font size
            font_size = content_area.value_of_css_property('font-size')
            print(f"Content Area Font Size: {font_size}")
        else:
            print("No content area found using the provided selectors or fallback method.")

    finally:
        # Clean up: close the browser window
        driver.quit()

if __name__ == "__main__":
    # URL to extract font sizes from
    url = "https://example.com"
    get_font_size_from_content_area(url)
