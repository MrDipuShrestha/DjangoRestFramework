import requests

endpoints = "http://localhost:8000/api/product/1/update/"

data= {
    "title": "hello world from the dipesh shrestha",
    "price": "99.99"
}

response =  requests.put(endpoints, json=data)


print(response.json())

