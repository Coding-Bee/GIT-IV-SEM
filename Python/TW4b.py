

class Person:

     def __init__(self,fname,lname,email):
          self.fname = fname
          self.lname = lname
          self.email = email

     def fullName(self):
          return "Full name is:"+self.fname+" "+self.lname
     

class Customer(Person):
     def __init__(self,fname,lname,email,cnum):
          Person.__init__(self,fname,lname,email)
          self.cnum = cnum


class Employee(Person):
     def __init__(self,fname,lname,email,panNo):
          Person.__init__(self,fname,lname,email)
          self.panNo = panNo
          
