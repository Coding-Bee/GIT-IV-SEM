def Add(stDict,n):
    
    for i in range(n):
        mkLst=[]
        usn = input("Enter USN:")
        for j in range(3):
            marks = input("Enter mks:")
            mkLst.append(marks)
        stDict[usn]=mkLst

def Delete(stDict):
    usn = input("Enter USN to be deleted:")
    del stDict[usn]

def Display(stDict):
    print(stDict)

def CompAvg(stDict):
    usn=input("Enter usn:")
    lst = stDict[usn]
    tempLst = lst.copy()
    tempLst.remove(min(tempLst))
    print(tempLst)
    avg=(int(tempLst[0])+int(tempLst[1]))/2.0
    print(avg)
    
def main():
    stDict={}
    n=int(input("Enter n:"))
    while(True):
        print("Enter 1.Add 2.Delete 3.Display 4.CompAvg 5.Exit")
        choice = int(input("Enter choice:"))
        if(choice == 1):
            Add(stDict,n)
        elif(choice == 2):
            Delete(stDict)
        elif(choice == 3):
            Display(stDict)
        elif(choice == 4):
            CompAvg(stDict)
        else:
            break
                
    
    


if __name__ == "__main__":
    main()
