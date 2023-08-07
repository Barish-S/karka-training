order=input("Enter The Order 1 : ")
order1=input("Enter The Order 2 : " )
user_food={"milk":5.5,"popcorn":3.5,"bread":2.5}
if (order=="milk" and order1=="popcorn") or (order=="popcorn" and order1=="milk"):
    print("Total Cost Rs",user_food["milk"]+user_food["popcorn"])
elif (order=="milk" and order1=="bread") or (order=="bread" and order1=="milk"):
    print("Total Cost Rs",user_food["milk"]+user_food["bread"])
elif (order=="popcorn" and order1=="bread") or (order=="bread" and order1=="popcorn"):
    print("Total Cost Rs",user_food["popcorn"]+user_food["bread"])
else:
    print("The Item Is Not Available")