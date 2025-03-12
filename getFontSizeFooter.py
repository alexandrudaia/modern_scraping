#pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def get_font_size_from_footer(url):
    # Set up the WebDriver
 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Load the webpage
        driver.get(url)

        # Try to identify the footer using the <footer> tag or a class name
        try:
            footer = driver.find_element(By.TAG_NAME, 'footer')
        except NoSuchElementException:
            try:
                footer = driver.find_element(By.CLASS_NAME, 'footer')
            except NoSuchElementException:
                print("No footer found on the page.")
                return

        # Get the computed font size
        if footer:
            font_size = footer.value_of_css_property('font-size')
            print(f"Footer Font Size: {font_size}")
        else:
            print("Footer element is present but could not be analyzed.")

    finally:
        # Clean up: close the browser window
        driver.quit()

if __name__ == "__main__":
    # URL to extract font sizes from
    url = "https://example.com"
    get_font_size_from_footer(url)
