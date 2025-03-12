from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_font_styles_from_paragraphs(url):
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Open the URL
    driver.get(url)

    try:
        # Wait for the page to fully load and stabilize
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)  # Optional: wait a bit longer for dynamic content

        # Find all paragraph tags
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')

        # Loop through each paragraph and fetch the font-style
        for paragraph in paragraphs:
            font_style = driver.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('font-style');", paragraph)
            print(f"Paragraph - Font style: {font_style}")

    except TimeoutException:
        print("Timed out waiting for page to load or elements to become available.")
    finally:
        # Close the browser
        driver.quit()

# Example usage
fetch_font_styles_from_paragraphs("https://www.example.com")
