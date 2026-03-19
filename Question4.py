# 14-03-2026 (Saturday)

'''
Automate Product Search on Myntra Using Class Name Locator
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get("https://www.myntra.com")
driver.maximize_window()
sleep(1)

driver.find_element(By.CLASS_NAME, "desktop-searchBar").send_keys("shoes")
driver.find_element(By.CLASS_NAME, "desktop-submit").click()

sleep(5)
driver.quit()
