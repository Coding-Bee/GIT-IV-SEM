def SE(n):
    
    prime_no=  [True] * n
    p=2
    
    while(p*p <= n):
        if(prime_no[p] == True):
            for i in range(p*2, n,p):
                prime_no[i] = False
        p=p+1
    
    prime_no[0] = False
    prime_no[1] = False
    
    for i in range(n):
        if(prime_no[i] == True):
            print(i)
    
def main():
    n=int(input("Enter n:"))
    SE(n)


if __name__ == "__main__":
    main()
