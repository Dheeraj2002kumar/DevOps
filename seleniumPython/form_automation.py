from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
import time

# setp 1: launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.maximize_window()
time.sleep(2)

# step 2: scroll to the form
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(1)

# step 3: fill out the example form
fname = driver.find_element(By.ID, "fname")
lname = driver.find_element(By.ID, "lname")

fname.clear()
lname.clear()

fname.send_keys("Dheeraj")
lname.send_keys("Kumar")

# step 4: submit the form (it opens in new tab)
submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_btn.click()

print("✅ Form filled and submitted successfully!")

time.sleep(4)
driver.quit()