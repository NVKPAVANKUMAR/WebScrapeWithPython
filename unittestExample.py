import json
import unittest
import HtmlTestRunner
import requests
from pprint import pprint
import ConfigParser
import os

from requests import HTTPError


def read_json(self, data_source):
    with open(data_source) as datafile:
        data = json.load(datafile)
        return data


def config_parser(self, header, parameter):
    config = ConfigParser.ConfigParser()
    config.read("configuration/config.ini")
    return config.get(header, parameter)


def download(self, url, output_file_path):
    response = requests.get(url, stream=True)
    handle = open(output_file_path, 'wb')
    for chunk in response.iter_content(chunk_size=512):
        handle.write(chunk)
    assert os.path.getsize(output_file_path) is not 0


class TestRequests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_base_url = "https://reqres.in"

    def test_get(self):
        usn = config_parser(self, "Credentials", "username")
        pas = config_parser(self, "Credentials", "password")
        r = requests.get(self.api_base_url + "/api/login",
                         auth=(usn, pas))
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("GET API Failed.", error)

    def test_get_singleUser(self):
        r = requests.get(self.api_base_url + "/api/users/2")
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("GET User API Failed.", error)
        print(r.content)

    def test_post(self):
        data = read_json(self, 'data/post_data.json')
        r = requests.post(self.api_base_url + "/api/users", data)
        pprint(r.text)
        try:
            assert r.status_code == 201
        except AssertionError as error:
            print("POST API Failed.", error)

    def test_put(self):
        data = read_json(self, "data/patch_data.json")
        r = requests.put(self.api_base_url + "/api/users/2", data)
        pprint(r.text)
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("PUT API Failed.", error)

    def test_patch(self):
        data = read_json(self, "data/patch_data.json")
        r = requests.patch(self.api_base_url + "/api/users/2", data)
        pprint(r.text)
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("PUT API Failed.", error)

    def test_delete(self):
        r = requests.delete(self.api_base_url + '/api/users/2')
        try:
            assert r.status_code == 204
        except AssertionError as error:
            print("DELETE API Failed.", error)

    def test_pass_parameter_url(self):
        payload = {'page': '2'}
        r = requests.get(self.api_base_url + '/api/users', params=payload)
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
        verbs = requests.options('http://www.prideparrot.com/aboutme')
        pprint(verbs.headers["Server"])

    # status of the resource and HTTP header information
    def test_head_usage(self):
        verbs = requests.head('http://www.prideparrot.com/aboutme')
        pprint(verbs.headers)

    def test_parse_response(self):
        r = requests.get('https://api.github.com/repos/requests/requests/issues/482')
        #  issue = json.loads(r.text)
        #  print(issue['title'])
        #  print(issue['comments'])
        comments = r.json()
        self.assertNotEqual(comments['labels'][0]['name'], None)
        assert comments['labels'][0]['name'] is not None

    def test_post_multipart_encoded_file_upload(self):
        url = 'http://httpbin.org/post'
        files = {'file': open('google_logo.jpg', 'rb')}
        r = requests.post(url, files=files)
        assert r.status_code == 200

    def test_download_file(self):
        demo_url = "https://demo.silverstripe.org/Security/login?BackURL=%2Fadmin%2Fpages%2F"
        google_url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
        download(self, demo_url, "downloaded_data.html")
        download(self, google_url, 'google_logo.jpg')

    def test_mock_api(self):
        try:
            url = "http://demo8060361.mockable.io/api/users/{0}".format(1)
            r = requests.options(url=url)
            print(r.text)
            print(r.headers["allow"])
        except HTTPError as e:
            print(e.message)

    def test_parse_json(self):
        with open("data/json_data.json") as f:
            data = json.load(f)
        assert (data["members"][1]["powers"][2]) == "Superhuman reflexes"

    def test_post_api(self):
        data = {'name': ['football', 'basketball'], 'job': ['leader', 'follower']}
        r = requests.post(self.api_base_url + "/api/users", data)
        print(r.text)
        try:
            assert r.status_code == 201
        except AssertionError as error:
            print("POST API Failed.", error)

    def test_get_api(self):
        url = 'http://pjody.mocklab.io/json/1'
        r = requests.get(url=url)
        #assert r.status_code == 201
        self.assertEqual( r.status_code, 200)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
