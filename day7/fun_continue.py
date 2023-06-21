import inspect
class Car:
    # this method is for car driving
    # this method is for car driving
    def drive(self):
        pass

car = Car()
print(inspect.getcomments(car.drive))
# print(car.drive)

# a = 10
# print(dir(a))

# def fun(a, b=10):
#     z = a+b
#     return z
# print(fun)
# print(fun.__code__.co_argcount)
# print(fun.__code__.co_varnames)
# print(dir(fun.__code__))
# dunder method
# print(fun.__defaults__)
# print(fun.__name__)

# fun.tester = 100

# print(fun)
# print(dir(fun))
# print(fun.tester)
