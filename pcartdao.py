import mysql.connector as sq
class cart:
    '''conn=sq.connect(host="localhost",user="root",password="")
    try:
        cur=conn.cursor()
        q1="use product"
        q2="create table if not exists cart(cid integer(10) AUTO_INCREMENT primary key,uid integer  references user(uid),pid integer references product(pid),quantity integer ,totalprice integer)"
        cur.execute(q1)
        print("Database Connected")
        cur.execute(q2)
        print("Table Created..")
    except sq.errors.DatabaseError as e:
        print(e)'''
    def __init__(self):
        self.conn=sq.connect(host="localhost",user="root",password="",database="product")
        self.cur=self.conn.cursor()
    def insertproduct(self,qty,pid,uid):
        try:
            q2="select * from product where pid = %s"
            val= (pid,)
            self.cur.execute(q2,val)
            d=self.cur.fetchall()
            #print("=======================================")
            #print("CId"+"\t"+"PID"+"\t"+"UID"+"\t"+"quantity"+"\t"+"price")
            #print("=======================================")
            #for i in d: 
            #        for j in i:
            #            print(j,end="\t")
            #        print("\n")
            
            for i in d:
                totalprice = qty * i[3]
            q1="insert into cart(uid,pid,quantity,totalprice) values(%s,%s,%s,%s)"
            val=(uid,pid,qty,totalprice)
            self.cur.execute(q1,val)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def displaycart(self):
        try:
            q1="select * from cart"
            self.cur.execute(q1)
            d=self.cur.fetchall()
            print("=======================================")
            print("CId"+"\t"+"UID"+"\t"+"PID"+"\t"+"quantity"+"\t"+"price")
            print("=======================================")
            if(len(d)==0):
                print("Cart Empty...")
            else:
                for i in d: 
                    for j in i:
                        print(j,end="\t")
                    print("\n")
        except Exception as e:
            print(e)
    def displaycheckout(self,id):
        try:
            q1="select pid,quantity,totalprice from cart where pid=%s"
            val=(id,)
            q2="Select pname,price from product where pid=%s"
            val2=(id,)
            self.cur.execute(q1,val)
            d=self.cur.fetchall()
            self.cur.execute(q2,val2)
            data=self.cur.fetchall()
            j=data[0]
            i=d[0]
            print("product id:",i[0])
            print("product Name:",j[0])
            print("Product Price(each)",j[1])
            print("Total Quantity:",i[1])
            print("Total Price:",i[2])
        except Exception as e:
            print(e)
    def checkid(self,id):
            q1="select pid from cart"
            self.cur.execute(q1)
            d=self.cur.fetchall()
            for i in d:
                if i[0]==id:
                    return True
            return False        