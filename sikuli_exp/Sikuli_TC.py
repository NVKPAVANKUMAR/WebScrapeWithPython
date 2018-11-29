import unittest

from selenium import webdriver


class TestSikuli(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

    def test_doLogin(self):
        self.driver.get("https://demo.moodle.net/login/index.php")

