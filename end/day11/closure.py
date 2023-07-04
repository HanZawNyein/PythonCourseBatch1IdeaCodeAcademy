def fun(n):
    def add(data):
        return data+n
    return add

add = fun(20)
# print(add)
# print(add.__closure__)
# print(add.__closure__[0].cell_contents)

# def outer():
#     data = "outer"
#     def inner():
#         return data
#     return inner()

# fun = outer()
# print(fun.__closure__())

# nested fun
# variable refer
# return inner fun from outer

# closure = outer()
# del outer
# print(closure)

