import csv
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

quote_page = 'https://www.x-rates.com/calculator/?from=USD&to=INR&amount=1'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
price_box = soup.find('span', attrs={"class": 'ccOutputRslt'})
price = price_box.text.strip("INR")
with open("CurrencyValue.csv", 'ab') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["USD2INR", price, datetime.now()])

