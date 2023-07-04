def outer():
    d = "outer"
    def inner():
        nonlocal d
        d = "inner"
        print(d,"inner")
    inner()
    print(d,"outer")

outer()