n=int(input("Enter The Number: "))
for i in range(n*n,0,-1):
    if i%n==0:
        print("")
    print(i,end=' ')