g = 10
def fun():
    global g
    g = 20
    print(g,"fun")

fun()
print(g,"global")