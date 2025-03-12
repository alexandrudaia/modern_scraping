from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fetch_font_styles(url):
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Open the URL
    driver.get(url)

    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # List of header tags
    headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    # Loop through each header type and fetch elements
    for header in headers:
        elements = driver.find_elements(By.TAG_NAME, header)
        for element in elements:
            # Get the computed font-style using JavaScript
            font_style = driver.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('font-style');", element)
            print(f"{header.upper()} - Font style: {font_style}")

    # Close the browser
    driver.quit()

# Example usage
fetch_font_styles("https://www.example.com")
