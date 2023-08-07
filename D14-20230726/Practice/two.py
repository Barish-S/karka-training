get_num1=int(input("First No: "))
get_num2=int(input("Second No: "))
def max(num1,num2):
    if num1>num2:
        if num1%2==0:
            print(num1,"Even")
        else:
            print(num1,"Odd")
    elif num2>num1:
        if num2%2==0:
            print(num2,"Even")
        else:
            print(num2,"Odd")
max(get_num1,get_num2)