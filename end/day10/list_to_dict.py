names = ["han",'zaw','nyein']

# new_dict = dict()
# for name in names:
#     new_dict[name]=len(name)

new_dict = {name:len(name) for name in names}
# print(new_dict) {'han': 3, 'zaw': 3, 'nyein': 5}
print(new_dict.get("han",0.0))
print(new_dict)
# print()
jj = new_dict.setdefault("jj",10)
if isinstance(jj,float):
    print("JJ is int")
# print(new_dict)