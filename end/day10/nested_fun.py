def outer(a):
    # print(a)
    def inner(b):
        # print(b)
        print(a,b)
    return inner

outer(10)(20)
