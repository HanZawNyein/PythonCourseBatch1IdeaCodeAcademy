class Employee:
    def __init__(self, name, age, position) -> None:
        self.name = name
        self.age = age
        self.position = position

    def __gt__(self, other):
        return self.age > other

    def __ge__(self, other):
        return self.age >= other

    def __lt__(self, other):
        return self.age < other

    def __le__(self, other):
        return self.age <= other

    def __eq__(self, other):
        print("*"*10)
        return self.age == other
    def __ne__(self, other):
        print("*"*10)
        return self.age != other


if __name__ == "__main__":
    employee1 = Employee("A", 10, "Junior")
    print(employee1 != 10)
    # print(employee1 < 5)
