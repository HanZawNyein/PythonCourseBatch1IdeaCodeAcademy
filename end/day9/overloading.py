class A:
    def __init__(self,number) -> None:
        self.number = number

    def __add__(self,other):
        return self.number+other
    
    def __len__(self):
        return 10

    def __int__(self):
        return 100

if __name__== "__main__":
    a = A(number=10)
    print(int(a))
    # print(len(a))    # print(a)
    # a+=10
    # print(a)