import csv
     
def srchAuthor(author):
     with open("Book.csv","r",newline="")as file:
          reader = csv.reader(file)
          for row in reader:
               if(str(row[1]) == author):
                    print(row)

def srchPrice(price):
     with open("Book.csv","r",newline="")as file:
          reader = csv.reader(file)
          for row in reader:
               if(int(row[3]) < price):
                    print(row)


def srchTitleWord(word):
     with open("Book.csv","r",newline="")as file:
          reader = csv.reader(file)
          for row in reader:
               if(word in  row[1]):
                    print(row)

def saveInfoCSV(bookLst):
     with open("Book.csv","w",newline="")as file:
          writer = csv.writer(file)
          writer.writerows(bookLst)
          

def readInfo():
     
     '''
     bookLst=[]
     n=int(input("Enter num of books:"))
     for i in range(n):
          book=[]
          book.append(input("Enter book num"))
          book.append(input("Enter book title"))
          book.append(input("Enter book author"))
          book.append(int(input("Enter book price")))
          bookLst.append(book)
     print(bookLst)
     '''
     #We will read info a static list
     bookLst = [['123','aaaa','bbb',1000],['234','cccc','ddd',2000]]
     for row in bookLst:
          if( row[3] <= 0):
               raise ValueError("Price should be more than Zero")
               
     return bookLst
     
def main():

     bookLst = readInfo()
     saveInfoCSV(bookLst)
     while(True):
          print("Srch by: 1.Author 2.Price 3.Title 4.Exit")
          choice = int(input("Enter choice"))
          if(choice == 1):
               author = input("Enter author")
               srchAuthor(author)
          elif(choice == 2):
               price = int(input("Enter price"))
               srchPrice(price)
          elif(choice == 3):
               word = input("Enter word:")
               srchTitleWord(word)
          else:
               break


if __name__ == "__main__":
     main()
