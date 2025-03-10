import requests

endpoints = "http://localhost:8000/api/product/2"


response =  requests.get(endpoints)


print(response.json())

