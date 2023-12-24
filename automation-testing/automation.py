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
button_text = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
print(button_text.get_attribute('innerHTML'))

# selectors are ways to grab items in a website, tags, class, ids etc
# find and use selenium cheat sheets

assert 'Show Message' in chrome_browser.page_source
#to check the whole page source for better checking.



