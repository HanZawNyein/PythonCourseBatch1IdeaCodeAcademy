#  python --> json
# dict --> object
# list --> arrary
# str --> string
# True --> true
# False --> false
# None --> null

import json

# values = '{"name":null,"age":20}'
# data = json.loads(values)
# print(data)

# python --> json = Serialization JSON --> dump,dumps
values = {"name":"Han","age":20}
# with open("data.json","w") as f:    
#     json.dump(values,f)
# print(type(json.dumps(values)))
json_data = json.dumps(values)

# json --> python = Deserializing JSON --> load,loads
# with open("data.json","r") as f:
#     data = json.load(f)
#     print(data)

data = json.loads(json_data)
print(data)
print(type(data))
