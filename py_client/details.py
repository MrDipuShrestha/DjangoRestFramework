import requests

endpoints = "http://localhost:8000/api/product/1"


response =  requests.get(endpoints)


print(response.json())

