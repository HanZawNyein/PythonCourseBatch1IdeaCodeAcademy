# data = ["Hello World",1,2,3,4,5,"HaZ"]
#               0     1 2 3,...
# # ...3,2,1,0,-1,-2,-3,...
# print(data[-2])

# list[list]
# data = [[2,3,4],[5,[6],7],[9,10,11]]
# # print(data[1][1][0])
# print(data)
# data[0].remove(3)
# print(data)

# data = [5,4,3,5,6]
# data.remove(5)
# data.remove(5)
# data.remove(6)
# print(data)

# data = ["b","c"]
# print(data)
# data.remove("a")
# data.pop(1)
# print(data)


# data = [1,2,3,4,5,6,7,8,9]
# print(data[2])
# data.pop(100)
# print(data[2])

# data = ["a","b","c","d"]
# print(data.index("ce"))

# data.append("e")
# print(f" append list is {data}")


# data = ["a","b","c","d"]
# print(f" Original list is {data}")
# second_data = ["f","g","h","i"]
# data += second_data # data = data + second_data
# # data.extend(second_data)
# print(f"extend data is {data}")

# data= ["a","b","c","d"]
# # data.append("e")
# print(data[-1])
# data.insert(-1,"e") #   ['a', 'b', 'e', 'c', 'd']
# print(data)

# data = ["a","b","c","d","a"]
# print(len(data))
# print(data.count("a"))
# data.reverse() # ['a', 'd', 'c', 'b', 'a']
# data.sort(reverse=True)
#['a', 'a', 'b', 'c', 'd'] asc
# ['d', 'c', 'b', 'a', 'a'] desc
# print(data)

data = ["a","b","c","d","a"]
# copy_data = data.copy()
# copy_data.append("zzzz")
data.clear()
print(data)
# print(copy_data)