a=[1,0,2,3,0,4,0,5,0]
b=0
for j in range(len(a)):
    for n in a:
        b=0+n
        if n==0:
            b.append(n)
print(b)