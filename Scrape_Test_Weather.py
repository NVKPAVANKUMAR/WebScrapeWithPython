import csv
from datetime import datetime
import urllib3
from bs4 import BeautifulSoup
import unittest
import HtmlTestRunner


class GetWeather(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_base_url = 'https://weather.com/en-IN/weather/today/l/INKA0259:1:IN'
        urllib3.disable_warnings()

    def test_weather_status(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.api_base_url)
        soup = BeautifulSoup(response.data, 'html.parser')
        weather_status = soup.find('div', attrs={"class": 'today_nowcard-phrase'})
        current_weather = weather_status.text
        with open("weather_update.csv", 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["BANGALORE", current_weather, datetime.now().strftime("%d-%m-%y %I:%M %p")])


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
