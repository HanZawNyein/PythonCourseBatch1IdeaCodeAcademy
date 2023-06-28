import operator as op 

# print(op.add(10,20))
operators = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
    "**":op.pow
}

if __name__ == "__main__":
    print(operators["**"](2,3))