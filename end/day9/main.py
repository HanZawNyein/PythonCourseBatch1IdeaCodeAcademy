# d = [1,2,3,4] # iterable objects
# res = filter(lambda x:x%2,d)
# print(list(res))
# new_dict = {"a":1,"b":2}

# def fun(key_value):
#     return key_value[1]*2

# print(list(map(lambda x:x[1]*2,new_dict.items())))

# result = []
# for i in new_dict.items():
#     result.append(fun(i))
# #     key,value = i[0],i[1]
# #     print(key,value)
# #     result.append(value*2)
# print(result)
    


# d = [1,2,3,4] # iterable objects
# new_dict = {"a":1,"b":2}

# def fun(key_and_value):
#     return key_and_value[1]*2

# new_data = map(lambda x:x[1]*4,new_dict.items())

# print(list(new_data))
# new_data = iter(d)
# print(next(new_data))
# print(next(new_data))

# print(new_data.__next__())
# print(new_data.__next__())

# for i in new_data:
#     print(i)
# print(new_data)
# for i in d:
#     print(i)