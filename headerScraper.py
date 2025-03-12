import requests
from bs4 import BeautifulSoup
import re

def get_font_properties(css, property_name):
    # Regular expression to find the font properties in CSS
    pattern = re.compile(r'{}\s*:\s*([^;]+)'.format(re.escape(property_name)))
    match = pattern.search(css)
    if match:
        return match.group(1).strip()
    return "Not specified"

def main(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first header (h1)
    header = soup.find('h1')
    if header:
        # Check for inline style first
        style = header.get('style')
        if style:
            font_size = get_font_properties(style, 'font-size')
            font_family = get_font_properties(style, 'font-family')
            font_color = get_font_properties(style, 'color')
            background_color = get_font_properties(style, 'background-color')
        else:
            # If no inline style, check within <style> tags
            styles = soup.find_all('style')
            css = ' '.join(style.text for style in styles)
            font_size = get_font_properties(css, 'font-size')
            font_family = get_font_properties(css, 'font-family')
            font_color = get_font_properties(css, 'color')
            background_color = get_font_properties(css, 'background-color')
        
        print(f"Font Size: {font_size}")
        print(f"Font Style: {font_family}")
        print(f"Font Color: {font_color}")
        print(f"Background Color: {background_color}")
    else:
        print("No h1 header found on the page,checking h2.")
        header = soup.find('h2')
        if header:
                     # Check for inline style first
            style = header.get('style')
            if style:
                font_size = get_font_properties(style, 'font-size')
                font_family = get_font_properties(style, 'font-family')
                font_color = get_font_properties(style, 'color')
                background_color = get_font_properties(style, 'background-color')
            else:
                # If no inline style, check within <style> tags
                styles = soup.find_all('style')
                css = ' '.join(style.text for style in styles)
                font_size = get_font_properties(css, 'font-size')
                font_family = get_font_properties(css, 'font-family')
                font_color = get_font_properties(css, 'color')
                background_color = get_font_properties(css, 'background-color')
              
            print(f"Font Size: {font_size}")
            print(f"Font Style: {font_family}")
            print(f"Font Color: {font_color}")
            print(f"Background Color: {background_color}")     
        

if __name__ == "__main__":
    url = 'https://www.edition.cnn.com'  # Replace with the URL of your choice
    main(url)