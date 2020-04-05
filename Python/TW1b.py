
def Insert(qArr):
    item = input("Enter element to be inserted")
    qArr.append(item)

def Display(qArr):
    if(len(qArr)== 0):
        print("List is empty")
    else:
        print(qArr)
    
def Delete(qArr):
    if(len(qArr)== 0):
        print("List is empty")
    else:
        qArr.remove(qArr[0])
    
def main():
    qArr = []
    while(True):
        choice = int(input("Enter 1.Insert 2. Delete 3.Display 4.Exit:"))
        if(choice == 1):
            Insert(qArr)
        elif(choice == 2):
            Delete(qArr)
        elif(choice == 3):
            Display(qArr)
        else:
            print("Bye")
            break


if __name__ == "__main__":
    main()
