from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        """This is inner docs"""
        print("start - decorator")
        return func(*args,**kwargs)
    return inner

@wrapper
def fun(x,y):
    """This is DOCs"""
    return x**y 

if __name__ == "__main__":
    # result = fun(2,3)
    # print(result)
    print(fun.__name__)
    print(fun.__doc__)
