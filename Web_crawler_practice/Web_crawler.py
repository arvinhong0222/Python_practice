from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
PATH = 'C:\ChromeDriver\chromedriver.exe' # Path to the chromedriver.exe
driver = webdriver.Chrome(options=options, executable_path=PATH) # Open Chrome

driver.get('https://www.dcard.tw/f') # Open Dcard
search = driver.find_element(by = By.NAME, value = 'query') # Find the search bar
search.clear() # Clear the search bar
search.send_keys('Marvel') # Input the keyword
driver.find_element(by = By.CLASS_NAME, value = "sc-husrwi.kZacXU.sc-e6ba31f5-7.bGsqNk").click()
# Click the search button

# Wait for the page to load
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-da81b671-1.ePdEXk"))
)

time.sleep(1) # Wait for the page to load

titles = driver.find_elements_by_class_name("sc-b205d8ae-3") # 
# Find the titles of the posts
for title in titles:
    print(title.text)

driver.find_element(by = By.LINK_TEXT, value = "#有雷 #奇異博士 之恐怖片探討").click()  # Click the first article
driver.back() # Go back to the previous page
driver.back()
driver.forward() #  Go forward to the next page

time.sleep(1)
driver.quit() # Close the browser