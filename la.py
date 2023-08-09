nums_list = [20,15,2, 5, 8, 9, 3, 35, 7,10]
max=0
min=nums_list[3]
for n in nums_list:
    if n>max:
        max=n
    if n<min:
        min=n
re=max-min
print(re,"(",min,"-",max,")")