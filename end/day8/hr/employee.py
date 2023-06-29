class Employee:
    def __init__(self, name, age, position) -> None:
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self) -> str:
        return f"Employee({self.name})"

    def __add__(self, other):
        return f"Employee{self.name, other.name}"

    def __iadd__(self, other):  # inplace add
        return f"Employee i add {self.name, other.name}"

    def __sub__(self, other):
        return "this is sub"

    def __isub__(self, other):
        return "this is inplace sub"

    def __mul__(self, other):
        return self.age * other.age

    def __imul__(self, other):
        print(other)
        return (self.age* other.age)//2

    def __truediv__(self, other):
        return self.age/other.age
    def __itruediv__(self, other):
        return other.age/self.age

if __name__ == "__main__":
    employee1 = Employee("A", 10, "Junior")
    employee2 = Employee("B", 30, "Senior")
    employee1/=employee2
    print(employee1)
    # employee1 = employee1- employee2
    # employee1 -= employee2
    # result = employee1 * employee2
    # print(result)
    # employee1*=employee2
    # print(employee1)
    # print(employee3)
