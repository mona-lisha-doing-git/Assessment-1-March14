# 14-03-2026 (Saturday)

'''
Automate Login Process on Facebook Using CSS Selectors
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name= 'email']").send_keys("abc@gmail.com")
sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[name= 'pass']").send_keys("hello world this is my password")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "div[aria-label= 'Log in']").click()
sleep(5)
driver.quit()
