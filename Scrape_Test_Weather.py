import csv
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
import unittest
import HtmlTestRunner


class TestGetWeather(unittest.TestCase):
    def test_weather_status(self):
        weather_page = 'https://weather.com/en-IN/weather/today/l/INKA0259:1:IN'
        page = urllib2.urlopen(weather_page)
        soup = BeautifulSoup(page, 'html.parser')
        weather_status = soup.find('div', attrs={"class": 'today_nowcard-phrase'})
        current_weather = weather_status.text.strip("")
        with open("weather_update.csv", 'ab') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["BANGALORE", current_weather, datetime.now().strftime("%d-%m-%y %I:%M %p")])


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
