userDetails = [{
    "name" : "saravana",
    "e_mail" : "saravana@gmail.com",
    "password" : "saravan@123",
},
{
    "name" : "benish",
    "e_mail" : "benish@gmail.com",
    "password" : "benish@123",
},
{
    "name" : "kabeesh",
    "e_mail" : "kabeesh@gmail.com",
    "password" : "kabeesh@123",
},
{
    "name" : "naathan",
    "e_mail" : "naathan@gmail.com",
    "password" : "naathan@123",
}]
get_input=input("Login or Register :")
def inputName(choice,user):
    if choice=="login":
        mail=input("Enter The e-mail: ")
        password=input("Enter The Password :")
        for check in user:
            eid=check["e_mail"]
            pswd=check["password"]
            if mail==eid and password==pswd:
                print("User Name:",check["name"])
            else:
                print("The Account Is Not Found")
    elif choice=="register":
         name=input("Enter Your Name: ")
         e_mail=input("Create Your Mail ID: ")
         reg_password=input("Enter Your Password: ")
         c_password=input("Confirm Password : ")
         if reg_password==c_password:
             user.append({"name" :name,"e_mail" : e_mail,"password" : c_password})
             print("Your Registered")
             return user
print(inputName(get_input,userDetails))