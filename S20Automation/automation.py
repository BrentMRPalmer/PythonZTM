# Automation

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
chrome_browser = webdriver.Chrome()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# print('Selenium Easy Demo' in chrome_browser.title)

button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
# print(button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
 
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')
time.sleep(2)

show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text