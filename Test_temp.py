import unittest

import requests


class TestRequests(unittest.TestCase):

    def test_get_api(self):
        url = 'http://pjody.mocklab.io/json/1'
        r = requests.get(url=url)
        # assert r.status_code == 201 (hard assertion - aborts execution)
        self.assertEqual(r.status_code, 200)

    def test_post_api(self):
        url = 'http://pjody.mocklab.io/json/1'
        r = requests.get(url=url)
        # assert r.status_code == 201(soft assertion - error handling and logging)
        self.assertEqual(r.status_code, 200)
