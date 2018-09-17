import csv
import urllib
import urllib2
from datetime import datetime

import HtmlTestRunner
from bs4 import BeautifulSoup
import unittest


class TestGetConversionValue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_base_url = 'https://www.x-rates.com/calculator/'

    def test_currency_value(self):
        query_args = {'from': 'USD', 'to': 'INR', 'amount': '1'}
        data = urllib.urlencode(query_args)
        request = urllib2.Request(self.api_base_url, data)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')
        price_box = soup.find('span', attrs={"class": 'ccOutputRslt'})
        price = price_box.text.strip("INR")
        with open("CurrencyValue.csv", 'ab') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["USD2INR", price, datetime.now()])


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
