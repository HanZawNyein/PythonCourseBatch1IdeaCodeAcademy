# for i in range(0,10):
#     print(i)

# def area(a,b):
#     return a*b

# print()
# first = area(10,20)
# second = area(50,70)
# print(first,second)
# def updater(d):
#     z = d.copy()
#     z[2]*=100
#     return z

# data  = [1,2,3,4,5,6,7,8,9]
# updater(data)
# print(data)

# x =100
# def xyz(a,b):
#     return x*a*b

# print(xyz(10,10))
# x = 200
# print(xyz(10,10))

# def area(x,y):
#     return x*y

# def xyz(x,y,fn):
#     z= fn(x,y)*15
#     return z

# print(xyz(10,10,area))

# a,b = 10,15
# # b = 15
# a,b=b,a
# print(a,b)

# (a,b,c,d) = [1,2,3,4]
# print(a,b,c,d)

# a,b,c,d,e = "Hello"
# print(a,b,c,d,e)

# a,*b = "Hello"
# print(a,b)

# zz = 1,2,3,4,5,6,7,8,9
# a,*b,c = zz
# print(type(zz))
# print(a,b,c)

# zz = [1,2,3,"HereTester"]
# a,*b,x = zz
# print(a,b,x,y,z)

def fun(a,b,*,c):
    print(a,b,c)

result = fun(10,20,c=30)
# print(result)