class A:
    def add(self,a,b):
        return a+b

class B:
    def sub(self,a,b):
        return a-b 

class C(A,B):
    ...

if __name__ == "__main__":
    c = C()
    print(c.sub(10,20))
    # a = A()
    # a.add()