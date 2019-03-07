from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('http://google.com')

search_box = chrome.find_element_by_name('q')
search_box.send_keys("Nice")
search_box.send_keys(Keys.RETURN)