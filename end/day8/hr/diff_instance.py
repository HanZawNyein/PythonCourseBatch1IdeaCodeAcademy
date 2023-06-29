class Employee:
    def __init__(self, name, age, position) -> None:
        self.name = name
        self.age = age
        self.position = position

    def __add__(self, other):
        return self.age + other

    def __iadd__(self, other):
        return (self.age + other) - 1

    def __radd__(self, other):  #
        return self.age + other


if __name__ == "__main__":
    employee1 = Employee("A", 10, "Junior")
    employee1 += 1
    # print(employee1 + 2)
    print(2 + employee1)
    # a+b
#     a = operand
# b = operand
# special, dunder method