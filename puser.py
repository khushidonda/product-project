from pusermodel import user
from puserdao import userdao
from pproductdao import productdao
from pcartdao import cart
def loginmenu(id):
    print("================Welcome to Login-Menu===================")
    while True:
        pdao=productdao()
        print("\t1.Display Products")
        print("\t2.Add To Cart")
        print("\t3.search by NAME")
        print("\t4.search by HIGHER PRICE")
        print("\t5.search by LOWER PRICE")
        print("\t6.search between HIGH & LOW")
        print("\t7.search by category")
        print("\t8.checkout")
        print("\t0.exit")
        c=cart()
        ch1=int(input("enter choice:"))
        if ch1==1:
            pdao.display()
        elif ch1==2:
            pdao.display()
            pid=int(input("Enter Id :"))
            status=pdao.checkid(pid)
            if (status):
                qty=int(input("Enter Total Quantity:"))
                stat=c.insertproduct(qty,pid,id)
                if(stat):
                    print("Added Into Cart....")
                else:
                    print("Some Error...")
            else:
                print("No Product With This Id...")
            
        elif ch1==3:
            name=input("Enter Product Name To Search:")
            status=pdao.checkname(name)
            if(status):
                pdao.searchbyname(name)
            else:
                print("Data Not Found....")
        elif ch1==4:
            p=int(input("enter price:"))
            pdao.searchbyhprice(p)
        elif ch1==5:
            p=int(input("enter price:"))
            pdao.searchbylprice(p)
        elif ch1==6:
            low=int(input("enter lower value:"))
            higher=int(input("enter higher value:"))
            pdao.searchbyprange(low,higher)
        elif ch1==7:
            category=input("Enter category to search:")
            status=pdao.checkcategory(category)
            if(status):
                pdao.searchbycategory(category)
            else:
                print("Data Not Found....")
        elif ch1==8:
            c.displaycart()
            id=int(input("enter id you want to buy..."))
            status=c.checkid(id)
            if(status):
                c.displaycheckout(id)
            else:
                print("nf")
        elif ch1==0:
            print("exit user login...")
            break
        else:
            print("invalid input...")
def usermenu():
    while True:
        print("\n=========== Welcome to User Menu ===============n")
        print("1.Register")
        print("2.Login")
        print("0.Back to Main Screen")
        udao = userdao()
        ch = int(input("Enter your choice : "))
        
        if(ch==1):
            uname=input("Enter Name:")
            email=input("Enter Email:")
            passw=input("Enter Password:")
            u=user(uname,email,passw)
            status=udao.insertuser(u)
            if(status):
                print("Registered succssfully...")
            else:
                print("Failed To Register....")
        elif(ch==2):
            cnt=0
            uname=input("Enter Name:")
            passw=input("Enter Password:")
            status=udao.loginuser(uname,passw)
            id = status[1]
            if(status[0]):
                print("Login succssfully done")
                print("*****************Welcome  "+uname+"*********************")
                loginmenu(id)
            else:
                print("Please Check Your Creditionals")
        elif(ch==0):            
            break
        else:
            print("invalid choice")