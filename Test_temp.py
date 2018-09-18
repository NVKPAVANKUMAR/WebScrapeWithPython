import sys
import unittest

import requests
import platform

import urllib3


class TestRequests(unittest.TestCase):

    def test_get_api(self):
        http = urllib3.PoolManager()
        r = requests.get('https://weather.com/en-IN/weather/today/l/INKA0259:1:IN')
        print(r.text)
        #r = requests.get(url=url)
        # assert r.status_code == 201 (hard assertion - aborts execution)
        self.assertEqual(r.status_code, 200)

    def test_post_api(self):
        url = 'http://pjody.mocklab.io/json/1'
        r = requests.get(url=url)
        # assert r.status_code == 201(soft assertion - error handling and logging)
        self.assertEqual(r.status_code, 200)

        if sys.version_info > (2, 7):
            import simplejson as json
        else:
            import json
