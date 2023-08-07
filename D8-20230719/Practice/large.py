num1=int(input("No 1 : "))
num2=int(input("No 2 : "))
num3=int(input("No 3 : "))
if num1>num2>num3:
    print(num1,"Is Larger Number")
if num1<num2<num3:
    print(num3,"Is Larger Number")
if num1<num2>num3:
    print("The Large Number Is",num2)