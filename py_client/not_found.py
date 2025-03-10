import requests

endpoints = "http://localhost:8000/api/product/223454"


response =  requests.get(endpoints)


print(response.json())

