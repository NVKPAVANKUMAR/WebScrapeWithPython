import unittest
import requests


class TestRequests(unittest.TestCase):

    def test_get(self):
        r = requests.get("https://reqres.in/api/login", auth=('peter@klaven', 'cityslicka'))
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("GET API Failed.", error)

    def test_get_singleUser(self):
        r = requests.get("https://reqres.in/api/users/2")
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("GET User API Failed.", error)
        print(r.content)

    def test_post(self):
        r = requests.post("https://reqres.in/api/users", data={"name": "morpheus",
                                                               "job": "leader"})
        try:
            assert r.status_code == 201
        except AssertionError as error:
            print("POST API Failed.", error)

    def test_put(self):
        r = requests.put("https://reqres.in/api/users/2", data={"name": "morpheus",
                                                                "job": "zion resident"})
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("PUT API Failed.", error)

    def test_patch(self):
        r = requests.patch("https://reqres.in/api/users/2", data={"job": "leader"})
        try:
            assert r.status_code == 200
        except AssertionError as error:
            print("PUT API Failed.", error)

    def test_delete(self):
        r = requests.delete('https://reqres.in/api/users/2')
        try:
            assert r.status_code == 204
        except AssertionError as error:
            print("DELETE API Failed.", error)

    def test_pass_parameter_url(self):
        payload = {'page': '2'}
        r = requests.get('https://reqres.in/api/users', params=payload)
        print(r.headers)
        print("------------------------------------------------------------------")
        print(r.request.headers)

    def test_response_code(self):
        r = requests.get(
            'https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
        if r.status_code == requests.codes.ok:
            print(r.headers['content-type'])
        commit_data = r.json()
        # print(commit_data.keys())
        print(commit_data['committer'])
        print(commit_data['message'])

    @unittest.skip("Not working")
    def test_options_usage(self):
        verbs = requests.options(
            'https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
        print(verbs.headers['allow'])

    def test_parse_response(self):
        r = requests.get('https://api.github.com/repos/requests/requests/issues/482')
        #  issue = json.loads(r.text)
        #  print(issue['title'])
        #  print(issue['comments'])
        comments = r.json()
        self.assertNotEqual(comments['labels'][0]['name'], None)
        assert comments['labels'][0]['name'] is not None
