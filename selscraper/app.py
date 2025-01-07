import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no=sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#Use Nix environment variables
chrome_path = os.getenv("CHROME_PATH")
chromedriver_path = os.getenv("CHROME_DRIVER_PATH")

# Set Chrome binary location
chrome_options.binary_location = chrome_path

# Create WebDriver Instance
wd = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

# Get the main page
wd.get("https://www.wikipedia.org/")

# Assertion statement
assert "Wikipedia" in wd.title

# Print the entire HTML
# print(wd.page_source)

# Fetching the element by ID
input_element = wd.find_element(by="ID", value="searchInput")

# Sending keys
input_element.send_keys('ASD')

wd.quit()