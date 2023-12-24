from selenium import webdriver
from selenium.webdriver.common.by import By
# import By for By.CLASS_NAME
# webdriver allows to drive the web through code
# gotta keep the chrome driver in the same directorry. 

# if pip selenium installed globally no need to put path of chromedriver.  

chrome_browser = webdriver.Chrome()
# chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
#checks if str exists and stops code if false. 
assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
print(show_message_button.get_attribute('innerHTML'))
# for css selections, #higher element ID, '#id > .css_name'
# selectors are ways to grab items in a website, tags, class, ids etc
# find and use selenium cheat sheets
# $==0 in the inspect part is actually pointing to id, and can be opened in console of browser. 

assert 'Show Message' in chrome_browser.page_source
#to check the whole page source for better checking.

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear() #to clear first for best practice. 
user_message.send_keys('Hello there!!')

show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'Hello there!!' in output_message.text
#can do innerHTML or text
