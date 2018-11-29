from selenium import webdriver
import unittest


class Test(unittest.TestCase):
    def test_browser_invoke(self):
        driver = webdriver.Chrome("Drivers/chromedriver.exe")
        driver.get("http://www.google.com")
