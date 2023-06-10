import mysql.connector as sq
class productdao:
    '''
    try:
        conn=sq.connect(host="localhost",user="root",password="")
        cur=conn.cursor()
        q1="create database if not exists product"
        cur.execute(q1)
        print("DTB created")
        q2="use product"

        q3="create table if not exists product(pid integer AUTO_INCREMENT primary key,pname varchar(10),pdesc varchar(50),price integer,pcat varchar(30))"
        cur.execute(q2)
        cur.execute(q3)
        print("t created")
    except Exception as e:
        print(e)
        '''
    def __init__(self):
        self.conn=sq.connect(host="localhost",user="root",password="",database="product")
        self.cur=self.conn.cursor()
    def insert(self,p):
        try:
            q1="insert into product(pname,pdesc,price,pcat) values(%s,%s,%s,%s)"
            val=(p.pname,p.pdesc,p.pprice,p.pcat)
            self.cur.execute(q1,val)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def display(self):
        try:
            q1="select * from product"
            self.cur.execute(q1)
            d=self.cur.fetchall()
            print("=======================================")
            print("Id"+"\t"+"pname"+"\t"+"description"+"\t"+"price"+"\t"+"category")
            print("=======================================")
            for i in d: 
                    for j in i:
                        print(j,end="\t")
                    print("\n")
        except Exception as e:
            print(e)
    def searchbyname(self,name):
        try:
            q1="select * from product where pname=%s"
            val=(name,)
            self.cur.execute(q1,val)
            d=self.cur.fetchall()
            print("===============================================================")
            print("Id"+"\t"+"pname"+"\t"+"description"+"\t"+"price"+"\t"+"category")
            print("===============================================================")
            for i in d: 
                    for j in i:
                        print(j,end="\t")
                    print("\n")
        except Exception as e:
            print(e)
    def searchbycategory(self,cat):
        try:
            q1="select * from product where pcat=%s"
            val=(cat,)
            self.cur.execute(q1,val)
            d=self.cur.fetchall()
            print("===============================================================")
            print("Id"+"\t"+"pname"+"\t"+"description"+"\t"+"price"+"\t"+"category")
            print("===============================================================")
            for i in d: 
                    for j in i:
                        print(j,end="\t")
                    print("\n")
        except Exception as e:
            print(e)
    def searchbyhprice(self,p):
        try:
            q1="select * from product where price>%s"
            val=(p,)
            self.cur.execute(q1,val)
            d=self.cur.fetchall()
            print("===============================================================")
            print("Id"+"\t"+"pname"+"\t"+"description"+"\t"+"price"+"\t"+"category")
            print("===============================================================")
            if(len(d))!=0:
                    for i in d: 
                        for j in i:
                            print(j,end="\t")
                        print("\n")
            else:
                print("no data")
        except Exception as e:
            print(e)
    def searchbylprice(self,p):
        try:
            q1="select * from product where price<%s"
            val=(p,)
            self.cur.execute(q1,val)
            d=self.cur.fetchall()
            print("===============================================================")
            print("Id"+"\t"+"pname"+"\t"+"description"+"\t"+"price"+"\t"+"category")
            print("===============================================================")
            if(len(d))!=0:
                    for i in d: 
                        for j in i:
                            print(j,end="\t")
                        print("\n")
            else:
                print("no data")
        except Exception as e:
            print(e) 
    def searchbyprange(self,low,high):
        try:
            q1="select * from product where price>%s and price<%s"
            val=(low,high)
            self.cur.execute(q1,val)
            d=self.cur.fetchall()
            print("===============================================================")
            print("Id"+"\t"+"pname"+"\t"+"description"+"\t"+"price"+"\t"+"category")
            print("===============================================================")
            if(len(d))!=0:
                    for i in d: 
                        for j in i:
                            print(j,end="\t")
                        print("\n")
            else:
                print("no data")
        except Exception as e:
            print(e)

    def checkid(self,id):
            q1="select pid from product"
            self.cur.execute(q1)
            d=self.cur.fetchall()
            for i in d:
                if i[0]==id:
                    return True
            return False
    def checkname(self,name):
            q1="select pname from product"
            self.cur.execute(q1)
            d=self.cur.fetchall()
            for i in d:
                if i[0]==name:
                    return True

            return False
    def checkcategory(self,cat):
            q1="select pcat from product"
            self.cur.execute(q1)
            d=self.cur.fetchall()
            for i in d:
                if i[0]==cat:
                    return True
            return False
        
    def update(self,id1,n,p,d,c):
         try:
            q1="update product set pname=%s,pdesc=%s,price=%s,pcat=%s where pid=%s"
            val=(n,d,p,c,id1)
            self.cur.execute(q1,val)
            self.conn.commit()
            print("Data updated..")
         except Exception as e:
            print(e)
            print("Data Not updated.....")
    def delete(self,id1):
         try:
            q1="delete from product where pid=%s"
            val=(id1,)
            self.cur.execute(q1,val)
            self.conn.commit()
            print("Data Deleted")
         except Exception as e:
            print(e)
            print("Data Not Deleted")