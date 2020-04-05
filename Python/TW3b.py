def SearchStud(studLst):
     print("mks:"+studLst[0][2])
     range(len(studLst))
     lstgtEty = []
     for i in range(len(studLst)):
          if(int(studLst[i][2]) >= 80):
               lstgtEty.append(studLst[i][0])
     print(lstgtEty)
     
     with open("out.txt","w") as file:
          for i in lstgtEty:
               file.write(i)

     
def CheckValid(lst):
     usn  = lst[1]
     vUSN = usn[0:2]
     
     mks  = int(lst[2])
     coll = lst[3]

     if(vUSN.upper() != "GI" or coll.upper() != "GIT"):
          raise Exception("USN should start with GI and college should be GIT ")
          
     if(mks < 0 or mks > 100):
          raise Exception("Invalid marks")

     return 1     
     
     
     

def readFile(studLst):
     lst=[]
     valid = 0
     try:
          with open("in.txt","r") as infile:
               for line in infile:
                    line = line.replace("\n","")
                    lst = line.split(' ')
                    valid = CheckValid(lst)
                    
                    if(valid == 1):
                         studLst.append(lst)
                    else:
                         break
               if(valid == 1):
                    print(studLst)
          SearchStud(studLst)
     except ValueError:
          print("You entered invalid integer")
     except FileNotFoundError:
          print("File not found")

     
def main():
     studLst = []
     readFile(studLst)

if __name__ == "__main__":
     main()
