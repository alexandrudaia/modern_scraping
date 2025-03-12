from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def get_font_weights(url):
    # Setup the webdriver
  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the URL
    driver.get(url)

    # Dictionary to store the font weights
    font_weights = {}

    # Loop over each header tag
    for header in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        elements = driver.find_elements(By.TAG_NAME, header)
        weights = [element.value_of_css_property('font-weight') for element in elements]
        # Convert numerical weights to qualitative description
        weights = ['normal' if w == '400' else 'bold' if w == '700' else 'bolder' if w > '700' else 'lighter' if w < '400' else w for w in weights]
        font_weights[header] = weights

    # Quit the driver
    driver.quit()

    return font_weights

url = input("Enter the URL of the web page: ")
print(get_font_weights(url))
