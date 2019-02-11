import csv
import unittest
from datetime import datetime

import HtmlTestRunner
import urllib3
from bs4 import BeautifulSoup


def fetch_url_with_param(base_url, city):
    return base_url + city + ".html"


def fetch_initial_response(base_url):
    http = urllib3.PoolManager()
    response = http.request("POST", base_url)
    soup = BeautifulSoup(response.data, "html.parser")
    city_string = soup.find('select', attrs={'id': "search_city"})
    citylist = city_string.text.split()
    return citylist


def fetch_further_response(base_url, city_name):
    http = urllib3.PoolManager()
    response = http.request("POST", fetch_url_with_param(base_url, city_name))
    soup = BeautifulSoup(response.data, "html.parser")
    return soup


class TestGoldPriceValue(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global city_list
        city_list = []
        cls.base_url = 'https://www.goodreturns.in/gold-rates/'
        urllib3.disable_warnings()
        city_list = fetch_initial_response(cls.base_url)

    @unittest.SkipTest
    def test_url_fetch(self):
        url = fetch_url_with_param(self.base_url, "vijayawada")
        print(url)

    def test_gold_price(self):

        global city_list
        for i in range(len(city_list) - 1):
            soup = fetch_further_response(self.base_url, city_name=city_list[i])
            price_box = soup.find('strong', attrs={'id': "el"})
            price = price_box.text.replace("₹ ", "")
            with open("GoldPrice.csv", 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([datetime.now(), city_list[i], price])



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
