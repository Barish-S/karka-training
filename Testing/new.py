a=[1,0,2,3,0,4,0,5,0]
b=[]
for n in a:
    b.append(n)
    if n==0:
        b.append(0)
print(b)