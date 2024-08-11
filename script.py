from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ticker symbol input
ticker_symbol = input("Enter the ticker symbol: ")

# Setup Safari WebDriver
driver = webdriver.Safari()

# Maximize the browser window
driver.maximize_window()

# Navigate to the SEC filings search page
driver.get("https://www.sec.gov/search-filings")

# Wait for the page to load
time.sleep(3)  # Adjust the sleep time as necessary

# Locate the search input field by its ID
search_box = driver.find_element(By.ID, "edgar-company-person")

# Enter the ticker symbol into the search box
search_box.send_keys(ticker_symbol)

# Press Enter to initiate the search
search_box.send_keys(Keys.RETURN)

# Optionally, wait for a few seconds to let the search results load
time.sleep(2)  # Adjust as necessary

# Wait for search results to load
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h5[contains(text(), '10-K (annual reports) and 10-Q (quarterly reports)')]")))

# Click on the 10-K (annual reports) and 10-Q (quarterly reports) section
#expand_collapse_header = driver.find_element(By.XPATH, "//h5[contains(text(), '10-K (annual reports) and 10-Q (quarterly reports)')]//a[@class='expandCollapse']")
#expand_collapse_header.click()

# Wait for the section to expand
#time.sleep(2)  # Adjust as necessary

# Click on the "View all 10-Ks and 10-Qs" button
#view_all_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'View all 10-Ks and 10-Qs')]")))
#view_all_button.click()

# Optionally, wait for a few seconds to let the page load
time.sleep(50)  # Adjust as necessary

# Close the browser if needed
# driver.quit()
