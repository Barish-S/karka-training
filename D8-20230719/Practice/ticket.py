age=int(input("Enter The Age : "))
if age<=3:
    print("Free Ticket")
elif age>3 and age<12:
    pay=int(input("Pay $10: "))
    if pay==10:
        print("Paid $10")
elif age>=65:
    pay=int(input("Pay $12: "))
    if pay==12:
        print("Paid $12")
elif age>12 and age<65:
    pay=int(input("Pay $15: "))
    if pay==15:
        print("Paid $15")