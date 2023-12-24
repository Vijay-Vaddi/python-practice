from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear() #to clear first for best practice. 
user_message.send_keys('Hello there!!')

show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'Hello there!!' in output_message.text

chrome_browser.close()
chrome_browser.quit()
