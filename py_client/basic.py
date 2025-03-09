import requests

endpoints = "http://localhost:8000/api/"


response =  requests.get(endpoints, params={'abc': 123}, json={'message': "Hello there!"})

print(response.text)
print(response.status_code)

print(response.json())

