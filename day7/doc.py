# help(len)

# docstrings
# def fun(a: int, b: int) -> int:
#     # This is comment
#     """
#     PEP 8
#     This is fun docstrings
#     :param a:
#     :param b:
#     :return:
#     """
#     return a + b

# def fun(b=[1, 2, 3, 4, 5]):
#     z = []
#     for i in b:
#         z.append(i * 2)
#     return z


fun = lambda b=[1, 2, 3, 4, 5]: [(i * 2) for i in b]
# [6, 10, 14, 18]

if __name__ == "__main__":
    data = [3, 5, 7, 9]
    result = fun(data)
    print(id(data))
    print(id(result))
    # print(fun(10, 20))
    # help(fun)
