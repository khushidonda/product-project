from puser import usermenu
from padmin import login
while True:
    print("1.admin")
    print("2.user")
    print("0.exit")
    print()
    ch=int(input("Enter Choice:"))
    if(ch==1):
        login()
    elif (ch==2):
        usermenu()
    elif(ch==0):
        break
    else:
        print("Invalid choice...")
        