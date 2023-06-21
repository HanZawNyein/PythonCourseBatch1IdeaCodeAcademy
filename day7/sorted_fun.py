# help(sorted)

# shopping_mall = ["A", "F", "E", "c"]
# print(ord(shopping_mall[0]),ord(shopping_mall[1]))
# print(sorted(shopping_mall, key=lambda x: x.upper(), reverse=True))

# book_shop = {'bookC': 200, "bookB": 100, "bookA": 150}
# book_shop["bookB"]
# print(sorted(book_shop, key=lambda x: book_shop[x],reverse=True))

str_test = ['BbookC', 'AbookA', 'CbookB']
res = sorted(str_test,key=lambda x:x[-1])
print(res)
