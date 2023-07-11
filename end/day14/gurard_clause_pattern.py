
# @lambda _:_()
def go_online(connection,paid,internet,online):
    if not connection:
        return "No Internet Connection"
    
    if not paid:
        return "Not Paid"
    
    if not internet:
        return "no internet"

    if not online:
        return "offline"

    return "user is online..."

if __name__ == "__main__":
    connection,paid,internet,online = True,True,True,True
    result = go_online(connection,paid,internet,online)
    print(result)