from selenium import webdriver
from django.test import TestCase


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
        assert 'To-Do' in self.browser.title
    
