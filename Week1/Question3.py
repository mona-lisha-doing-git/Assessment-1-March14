# 14-03-2026 (Saturday)

'''
Automate Text Field Entry Using ID Locator
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get("https://www.naukri.com")
driver.maximize_window()
sleep(1)

driver.find_element(By.ID, "register_Layer").click()
sleep(2)

driver.find_element(By.ID, "name").send_keys("Monalisha Kalita")
sleep(2)
driver.find_element(By.ID, "email").send_keys("monalisha@gmail.com")
sleep(2)
driver.find_element(By.ID, "password").send_keys("This is a password input!")
sleep(5)
driver.quit()
