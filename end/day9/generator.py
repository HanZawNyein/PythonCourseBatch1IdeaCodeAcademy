def gen():
    yield 10
    yield 20
    yield 70

test = gen()
print(next(test))
print(next(test))
print(test.__next__())
