import requests
import json
try:
    context ={
        ""
    }
    response_obj = requests.post("https://dummyjson.com/products/add",data=context)
    if response_obj.status_code == 200:
        print(response_obj.json())
        # data = json.loads(response_obj.content)
        # print(type(data))
except Exception as e:
    print(e)