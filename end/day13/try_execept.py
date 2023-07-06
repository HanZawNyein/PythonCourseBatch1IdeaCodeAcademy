try:
    a= 10
    a += 11
except Exception as e:
    print("Can't add int and str")
else:
    print("I am else")
finally:
    print("I am finally")