class A:
    def add(self,a,b):
        return a+b 
    
class B(A):
    def sub(self,a,b):
        return a-b 
    
class C(B): # subclass
    def div(self,a,b):
        return a/b 

class D:
    ...
    
if __name__ == "__main__":
    c = C()
    print(isinstance(c,D))
    # name = "hello"
    # print(isinstance(name,int))
    # print(issubclass(C,B))
    # print(c.add(50,10))