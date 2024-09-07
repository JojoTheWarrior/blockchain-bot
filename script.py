from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode

# Initialize WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the voting webpage
driver.get('https://ai.google.dev/competition/projects/wanderlust')  # Replace with the actual URL of the voting page

# Wait for the page to load
time.sleep(3)  # Adjust the wait time if necessary

# Find the button using a CSS selector or XPath and click it
vote_div = driver.find_element(By.CLASS_NAME, "gemini-voted-foreground")
vote_div.click()

# Optional: Wait after clicking the button
time.sleep(3)

# Close the browser
driver.quit()