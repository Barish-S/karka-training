n=int(input("Enter The Number: "))
for i in range(1,(n*n)+1):
    print(i,end=' ')
    if i%n==0:
        print("")

