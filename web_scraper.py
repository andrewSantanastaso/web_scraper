from selenium import webdriver

# Set the path to the chromedriver
driver= webdriver.Chrome()
driver.get('https://www.cnn.com')

# Get the title of the page
title = driver.find_element(by='css selector', value='header')
print(title.text)
