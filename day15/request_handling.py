import requests

try:
    data_response = requests.get("https://dummyjson.com/products")

    if data_response.status_code == 200:
        data = data_response.json()
        # print(data)
        # print(type(data))
except Exception as e:
    print(e)

# print(data_response.status_code) # 404 503
# print(dir(data_response))

# request methods
# GET - server info
# POST - create
# PUT - update
# DELETE - delete