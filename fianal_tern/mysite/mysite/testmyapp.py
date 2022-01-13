from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.keys import Keys
import time
#v1.2
class FunctionalTest(TestCase):

    # do something before test start
    def setUp(self):
        self.browser = webdriver.Chrome()

    # do something after test complete
    def tearDown(self):
        self.browser.quit()

    # our test function
    def test_get_url(self):
        self.browser.get('http://localhost:8000/myapp/')
        self.assertIn('To-Do', self.browser.title)
    #v 1.3
        input_field = self.browser.find_element_by_id('new_item')
        self.assertEqual('Input New Item', input_field.get_attribute('placeholder'))
        new_items = ['first item', 'second item']
        input_field.send_keys(new_items[0])
        input_field.send_keys(Keys.ENTER)
        time.sleep(1)

        list_div = self.browser.find_element_by_id('to-do-list')
        to_do_list = list_div.find_elements_by_tag_name('li')
        self.assertTrue(all(to_do.text == new_items[index] for index, to_do in enumerate(to_do_list)))

        input_field = self.browser.find_element_by_id('new_item')
        input_field.send_keys(new_items[1])
        input_field.send_keys(Keys.ENTER)
        time.sleep(1)
        
        list_div = self.browser.find_element_by_id('to-do-list')
        to_do_list = list_div.find_elements_by_tag_name('li')
        self.assertTrue(all(to_do.text == new_items[index] for index, to_do in enumerate(to_do_list)))


    
