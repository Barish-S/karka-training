no=[1,2,3,4,5,6]
odd=[]
even=[]
for n in no:
   if n%2==0:
      even.append(n)
   elif not n%2==0:
        odd.append(n)
print("Odd No :",odd)
print("Even No :",even)
