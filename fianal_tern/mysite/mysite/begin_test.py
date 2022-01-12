from selenium import webdriver
import time
#import unittest
browser = webdriver.Chrome()
browser.get('http://localhost:8000')
#unittest.TestCase.assertTrue(browser.get('http://localhost:8000'),msg='OK!')
assert 'The install worked successfully!' in browser.title
print('pass!')
browser.quit()