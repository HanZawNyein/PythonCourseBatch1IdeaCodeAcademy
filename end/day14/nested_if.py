connection,paid,internet,online = True,True,True,True

if connection:
    if paid:
        if internet:
            if online:
                print("online...")
            else:
                print("offline...")
        else:
            print("no internet")
    else:
        print("no paid")
else:
    print("no conection")