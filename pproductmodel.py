class product():
    def __init__(self,name="",price=0,desc="",cat=""):
        self.pname=name
        self.pprice=price
        self.pdesc=desc
        self.pcat=cat
    def __str__(self):
        return self.pname+" "+self.pdesc+" "+self.pcat+" "+str(self.price)
        
        