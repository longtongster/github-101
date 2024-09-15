import requests
from requests.exceptions import HTTPError, ConnectionError

response =  requests.post("https://httpbin.org/post", json={"key": "value"})
print(response.headers['Content-type'])
json_reponse = response.json()
print(json_reponse["data"])