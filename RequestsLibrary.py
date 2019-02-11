import unittest
from pprint import pprint
import requests
from unittestExample import config_parser
import pytest


class TestRequests(unittest.TestCase):
    r = None

    def test_get(self):
        try:
            usn = config_parser("Credentials", "username")
            pas = config_parser("Credentials", "password")
            self.r = requests.get("https://reqres.in/api/login",
                                  auth=(usn, pas))
            assert self.r.status_code == 201
        except AssertionError as error:
            print("GET API Failed.", error)
            print(self.r.status_code)
            print(self.r.headers['content-type'])
            print(self.r.encoding)
            print(self.r.text)
            print(self.r.content)

    @pytest.mark.skipif(1 == 2, reason="Condition passed")
    def test_JsonServer(self):
        self.r = requests.options("http://localhost:3000/posts")
        pprint(self.r.status_code)

    if __name__ == "__main__":
        unittest.main(verbosity=2)
