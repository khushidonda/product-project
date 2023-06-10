from pproductmodel import product
from pproductdao import productdao
aname="admin"
apass="a@123"
def login():
    name=input("Enter Name:")
    p=input("Enter Password:")
    if(aname==aname and apass==p):
        amenu()
    else:
        print("Please Check Your creditionals...")
def amenu():
    while True:
        pdao=productdao()
        print("\t1.insert")
        print("\t2.update")
        print("\t3.delete")
        print("\t4.search by NAME")
        print("\t5.search by HIGHER PRICE")
        print("\t6.search by LOWER PRICE")
        print("\t7.search between HIGH & LOW")
        print("\t8.Display")
        print("\t9.category")
        print("\t0.exit")
        ch=int(input("enter choice:"))
        if ch==1:
            pname=input("Enter Product Name:")
            pdesc=input("Enter Product Description:")
            pprice=input("Enter Product Price:")
            pcat=input("Enter Product Category:")
            p=product(pname,pprice,pdesc,pcat)
            status=pdao.insert(p)
            if(status):
                print("DATA INSERTED...")
            else:
                print("Data not inserted...")
        elif ch==2:
            id=int(input("Enter ID To update:"))
            status=pdao.checkid(id)
            if(status):
                name=input("Enter pname To Update:")
                d=input("Enter Description To Update:")
                p=input("Enter Price To Update:")
                cat=input("Enter category To Update:")
                pdao.update(id,name,p,d,cat)
            else:
                print("Data Not Found")

        elif ch==3:
            id=int(input("Enter ID To delete:"))
            status=pdao.checkid(id)
            if(status):
                pdao.delete(id)
            else:
                print("Data Not Found....")
        elif ch==4:
            name=input("Enter Product Name To Search:")
            status=pdao.checkname(name)
            if(status):
                pdao.searchbyname(name)
            else:
                print("Data Not Found....")
                
        elif ch==5:
            p=int(input("enter price:"))
            pdao.searchbyhprice(p)
        elif ch==6:
            p=int(input("enter price:"))
            pdao.searchbylprice(p)
        elif ch==7:
            low=int(input("enter lower value:"))
            higher=int(input("enter higher value:"))
            pdao.searchbyprange(low,higher)
        elif ch==8:
            pdao.display()
        elif ch==9:
            category=input("Enter category to search:")
            status=pdao.checkcategory(category)
            if(status):
                pdao.searchbycategory(category)
            else:
                print("Data Not Found....")
            
        elif ch==0:
            print("exit from admin.....")
            break
        else:
            print("Invalid Choice....")