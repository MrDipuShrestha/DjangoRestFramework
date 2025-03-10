import requests

endpoints = "http://localhost:8000/api/product/"

data={
    'title': 'This is the title'
}
response =  requests.get(endpoints, json=data)


print(response.json())

