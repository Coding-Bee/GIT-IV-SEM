from TW4bClass import Person,Employee,Customer



def dispData(per):
   if(isinstance(per, Customer)):
      print(per.fullName()+" is a Customer")
   else:
      print(per.fullName()+" is a Employer")



cust=Customer("Bill","Gates","bg@msn.com","custNo101")
emp=Employee("Michael","Dell","mike@dell.com","panNo101")
dispData(cust)
   








