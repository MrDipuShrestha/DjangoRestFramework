import requests



product_id = input("what is the is of the data you want to delete?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not a valid id.")

if product_id:
    endpoints = f"http://localhost:8000/api/product/{product_id}/delete/"
    response =  requests.delete(endpoints)


    print(response.status_code)

