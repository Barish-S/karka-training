salary=int(input("Enter The Salary: "))
if salary<=10000:
    hri=(salary*.20)
    da=(salary*.05)
    total=salary+hri+da
    print(total)
elif salary>10000 and salary<=20000:
    hri=(salary*.25)
    da=(salary*.07)
    total=salary+hri+da
    print(total)
elif salary>20000:
    hri=(salary*.3)
    da=(salary*.08)
    total=salary+hri+da
    print(total)