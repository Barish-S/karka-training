noList=[1,2.0,"hai","@",5,6,"&",8,9]
num=0
for no in noList:
    if type(no)==int:
        num = num+1
print("Numbers In MixedList : ",num)