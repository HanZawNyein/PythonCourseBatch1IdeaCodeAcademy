name = input("Enter Your name : ")
print(f"Hello {name},")

next = input("Do you want to continue ? (yes/No) :").lower()
if next == "yes":
    print("OK!")
else:
    print("Program is exited.")