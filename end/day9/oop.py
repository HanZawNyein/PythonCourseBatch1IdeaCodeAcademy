from multipledispatch import dispatch

@dispatch(int, int)
def add(x, y):
    print("int,int")
    return x + y

@dispatch(object, object,object)
def add(x, y,z):
    print("object, object")
    return "%s + %s" % (x, y)


add(10,10)