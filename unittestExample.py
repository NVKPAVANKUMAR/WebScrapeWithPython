import json
import unittest

from pyunitreport import HTMLTestRunner
import requests
from pprint import pprint
import ConfigParser


def test_read_json(self, data_source):
    with open(data_source) as datafile:
        data = json.load(datafile)
        return data


def test_config_parser(self, header, parameter):
    config = ConfigParser.ConfigParser()
    config.read("configuration/config.ini")
    return config.get(header, parameter)


class TestRequests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_baseurl = "https://reqres.in"

    def test_get(self):
        usn = test_config_parser(self, "Credentials", "username")
        pas = test_config_parser(self, "Credentials", "password")
        r = requests.get(self.api_baseurl + "/api/login",
                         auth=(usn, pas))
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("GET API Failed.", error)

    def test_get_singleUser(self):
        r = requests.get(self.api_baseurl + "/api/users/2")
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("GET User API Failed.", error)
        print(r.content)

    def test_post(self):
        data = test_read_json(self, 'data/post_data.json')
        r = requests.post(self.api_baseurl + "/api/users", data)
        pprint(r.text)
        try:
            assert r.status_code == 201
        except AssertionError as error:
            print("POST API Failed.", error)

    def test_put(self):
        data = test_read_json(self, "data/patch_data.json")
        r = requests.put(self.api_baseurl + "/api/users/2", data)
        pprint(r.text)
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("PUT API Failed.", error)

    def test_patch(self):
        data = test_read_json(self, "data/patch_data.json")
        r = requests.patch(self.api_baseurl + "/api/users/2", data)
        pprint(r.text)
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("PUT API Failed.", error)

    def test_delete(self):
        r = requests.delete(self.api_baseurl + '/api/users/2')
        try:
            assert r.status_code == 204
        except AssertionError as error:
            print("DELETE API Failed.", error)

    def test_pass_parameter_url(self):
        payload = {'page': '2'}
        r = requests.get(self.api_baseurl + '/api/users', params=payload)
        print(r.headers)
        print("------------------------------------------------------------------")
        print(r.request.headers)

    def test_response_code(self):
        r = requests.get(
            'https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
        if r.status_code == requests.codes.ok:
            print(r.headers['content-type'])
        commit_data = r.json()
        pprint(commit_data['committer'])
        pprint(commit_data['message'])

    # information about the communication option available for a resource.
    def test_options_usage(self):
        verbs = requests.options('http://www.prideparrot.com/aboutme ')
        pprint(verbs.headers['allow'])

    def test_head_usage(self):
        verbs = requests.head('http://www.prideparrot.com/aboutme ')
        pprint(verbs.headers)

    def test_parse_response(self):
        r = requests.get('https://api.github.com/repos/requests/requests/issues/482')
        #  issue = json.loads(r.text)
        #  print(issue['title'])
        #  print(issue['comments'])
        comments = r.json()
        self.assertNotEqual(comments['labels'][0]['name'], None)
        assert comments['labels'][0]['name'] is not None


if __name__ == '__main__':
    unittest.main(testRunner= HTMLTestRunner(output="example_dir"))
