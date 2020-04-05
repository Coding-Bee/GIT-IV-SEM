class Doctor:
     def __init__(self,name,worksAt):
          self.name = name
          self.worksAt = worksAt
          
     def setSalary(self):
          self.basicSal = 1000
          return self.basicSal

     def treatsPatients(self):
          print("I treat patients")

'''
Create a Pediatrician object(put  required parameters)
Call set salary method
'''



class Pediatrician(Doctor):
     def __init__(self,name,worksAt):
          Doctor.__init__(self,name,worksAt)
          
     def setSalary(self):          
          self.sal = Doctor.setSalary(self) + 5000
          print("Pediatrician:My salary is:"+str(self.sal))
       

     def treatsPatients(self):
          print("I specialize in treating small children")

class Cardiologist(Doctor):
     def __init__(self,name,worksAt):
          Doctor.__init__(self,name,worksAt)
          
     def setSalary(self):       
          self.sal = Doctor.setSalary(self) + 8000
          print("Cardiologist:My salary is:"+str(self.sal))

     def treatsPatients(self):
          print("I specialize in treating patients with heart disease")
