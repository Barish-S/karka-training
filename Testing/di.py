strg = "the quick brown fox jumps over the lazy dog the quick brown fox the"
dub=strg.split()
a={}
for n in dub:
    if n not in a:
        a[n]=1
    else:
        a[n]+=1
print(a)
