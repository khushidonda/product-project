class user:
    def __init__(self,uname="",email="",passw=0):
        self.name=uname
        self.email=email
        self.password=passw
    def __str__(self):
        return self.name+" "+self.email+" "+self.password
       
