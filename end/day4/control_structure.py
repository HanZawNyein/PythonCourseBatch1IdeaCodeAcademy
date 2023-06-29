#  if elif else

#  if (condition):
    # expression
# a = 10
# b = 10
# if a is b:
#     print(a)
# elif a == 10:
#     print("a == 10")
# else:
#     print("a is not b")


# loop
#  while loop
# for loop

# while (condition)

i = 0
# while i < 10:
#     print(i)
#     i +=1

# while True:
#     if i > 6:
#         break
#     i +=1

while True:
    i+=1
    if i%2:
        continue
    print("*",i,i//2)
    if i > 10:
        break
    