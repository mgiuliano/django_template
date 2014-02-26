from selenium import webdriver
import unittest


class DummyTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_connect_to_server(self):  
        self.browser.get('http://10.1.29.10:8888')
        self.assertIn('Django', self.browser.title)
