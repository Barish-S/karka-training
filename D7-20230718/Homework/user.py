name=(input("Enter Your Name : "))
gender=(input("Enter Your Gender : "))
age=int(input("Enter Your Age : "))
if age>60 and gender=="male":
    print("Hi Mr."+name,",You Are a Senior Citizen")
elif age>60 and gender=="female":
    print("Hi Miss."+name,",You Are a Senior Citizen")
elif age>=18 and gender=="male":
    print("Hi Mr."+name,",You Are an Adult")
elif age>=18 and gender=="female":
    print("Hi Miss."+name,",You Are an Adult")
elif age<18 and gender=="male":
    print("Hi Mr."+name,",You Are a Teenager")
elif age<18 and gender=="female":
    print("Hi Miss."+name,",You Are a Teenager")