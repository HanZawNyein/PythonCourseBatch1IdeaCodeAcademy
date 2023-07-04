

def outer(func):
    print("i am decorator") # before
    def inner(y,z):
        y*=2
        res = sum(func(y,z))
        return res
    return inner

# dec = outer(fun)
# print(dec(10,20))

@outer
def fun(y,z):
    return y,z

print(fun(10,20))

# def fun(x,y):
#     print(x,y)

# def dec(func):
#     print("i am decorator ",func)
#     def inner(x,y):
#         print("i am inner",x,y)
#         return func(x,y)
#     return inner

# result = dec(fun)(10,20)
# # result(10,20)