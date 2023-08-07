mail_id=input("Enter The Email : ")
password=int(input("Enter The Password : "))
if mail_id=="barish@gmail.com":
    pass
else:
    print("Wrong Email-ID")
if password==1428:
    pass
else:
    print("Wrong Password")
if mail_id=="barish@gmail.com" and password==1428:
    print("You Are Logged Succeefully")
elif mail_id!="barish@gmail.com" and password!=1428:
    print("Yoo are not authenticated")