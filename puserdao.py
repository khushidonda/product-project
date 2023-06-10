import mysql.connector as sq
class userdao:
    '''
    conn=sq.connect(host="localhost",user="root",password="")
    try:
        cur=conn.cursor()
        q1="use product"
        q2="create table if not exists user(uid integer AUTO_INCREMENT primary key,uname varchar(80),uemail varchar(30),upassword varchar(20))"
        cur.execute(q1)
        print("Database Connected")
        cur.execute(q2)
        print("Table Created..")
    except sq.errors.DatabaseError as e:
        print(e)
    '''
    def __init__(self):
        self.conn=sq.connect(host="localhost",user="root",password="",database="product")
        self.cur=self.conn.cursor()
    def insertuser(self,u):
        try:
            q1="insert into user(uname,uemail,upassword) values(%s,%s,%s)"
            val=(u.name,u.email,u.password)
            self.cur.execute(q1,val)
            return True
        except Exception as e:
            print(e)
            return False
    def loginuser(self,name,p):
        q1="select uid,uname,upassword from user"
        self.cur.execute(q1)
        d=self.cur.fetchall()
        for i in d:
            if(i[1]==name and i[2]==p):
                return (True,i[0])
        return False
    