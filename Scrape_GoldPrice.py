import unittest
import urllib3
from bs4 import BeautifulSoup
import HtmlTestRunner


class TestGoldPriceValue(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'https://www.goodreturns.in/gold-rates/vijayawada.html'
        urllib3.disable_warnings()

    def test_gold_price(self):
        http = urllib3.PoolManager()
        response = http.request("POST", self.base_url)
        soup = BeautifulSoup(response.data, "html.parser")
        date_box = soup.find('div', attrs={'id': "current-date"})
        price_box = soup.find('div', attrs={'id': "el"})
        print(date_box, price_box)
        price = price_box.text.strip('')
        print(price)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
