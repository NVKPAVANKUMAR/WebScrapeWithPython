import csv
import unittest
import urllib
from datetime import datetime
import HtmlTestRunner
import urllib3
from bs4 import BeautifulSoup


class TestGetConversionValue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_base_url = 'https://www.x-rates.com/calculator/'
        urllib3.disable_warnings()

    def test_currency_value(self):
        http = urllib3.PoolManager()
        response = http.request('POST', self.api_base_url, fields={'from': 'USD', 'to': 'INR', 'amount': '1'})
        soup = BeautifulSoup(response.data, features="lxml")
        price_box = soup.find('span', attrs={"class": 'ccOutputRslt'})
        price = price_box.text.strip("INR")
        with open("CurrencyValue.csv", 'ab') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["USD2INR", price, datetime.now()])


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
