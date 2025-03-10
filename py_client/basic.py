import requests

endpoints = "http://localhost:8000/api/"


response =  requests.post(endpoints, params={'abc': 123}, json={'title':'sayHello', 'content': "Hello World!", 'price': 'abd123'})

print(response.text)
print(response.status_code)

print(response.json())

