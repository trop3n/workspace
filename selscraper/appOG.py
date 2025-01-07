from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no=sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Create WebDriver Instance
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# Get the main page
wd.get("https://www.wikipedia.org/")

# Assertion statement
assert "Wikipedia" in wd.title

# Print the entire HTML
# print(wd.page_source)

# Fetching the element by ID
input_element = wd.find_element(by=By.ID, value="searchInput")

# Sending keys
input_element.send_keys('ASD')

search = wd.find_element(by=By.CLASS_NAME, value="pure-button")
wd.execute_script("arguments[0].click();", search)

# switching windows
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# assertion
assert "ASD - Wikipedia" in wd.title
# print("Successfully loaded the page ",wd.title)

# fetch and click
link_text = wd.find_element(By.LINK_TEXT, "Adaptive sofware development")
wd.execute_script("arguments[0].click();", link_text)

# switching window
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# assertion statement
assert "Adaptive software development - Wikipedia" in wd.title
# print("Successfully loaded the page", wd.title)

# fetch all elements with <p> tags
p_tags = wd.find_elements(by=By.TAG_NAME, value="p")

# printing the array with <p> tag elements
#print("Number of tags found: ", len(p_tags))

# extract text from all elements
text_lines = ''
for p_tag in p_tags:
    text_lines += p_tag.text

print(text_lines)