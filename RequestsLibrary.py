import unittest
from pprint import pprint

import requests

from unittestExample import config_parser


class TestRequests(unittest.TestCase):
    def test_get(self):
        try:
            usn = config_parser(self, "Credentials", "username")
            pas = config_parser(self, "Credentials", "password")
            r = requests.get("https://reqres.in/api/login",
                             auth=(usn, pas))
            assert r.status_code == 200
        except AssertionError as error:
            print("GET API Failed.", error)
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json())

    def test_JsonServer(self):
        r = requests.options("http://localhost:3000/posts")
        pprint(r.status_code)


if __name__ == "__main__":
    unittest.main(verbosity=2)
