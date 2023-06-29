_ = 10

for _ in range(10):
    ...

a = 10_000_000

try:
    pass
except Exception as _:
    print("Error")


data = 1,2,3,4,5
a,b,c,d,_ = data

a,*_,e =data
print(a,e)