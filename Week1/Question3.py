# 14-03-2026 (Saturday)

'''
Automate Search on YouTube Using Name Locator
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get("https://www.youtube.com")
driver.maximize_window()
sleep(1)

