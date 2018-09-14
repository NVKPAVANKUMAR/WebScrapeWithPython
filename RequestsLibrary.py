import requests

r = requests.get("https://reqres.in/api/login", auth=('peter@klaven', 'cityslicka'))
try:
    assert r.status_code == 201
except Exception as e:
    print("Assertion Failed. ", e)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
