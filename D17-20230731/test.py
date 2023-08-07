user_Details = [{
    "name" : "Saravana",
    "e_mail" : "saravana@gmail.com",
    "password" : "saravan@123",
    "hobbies":["Cricket","Volleyball"],
    "friend_list":["Saheen","Ashif","Safeek"]
},
{
    "name" : "Benish",
    "e_mail" : "benish@gmail.com",
    "password" : "benish@123",
    "hobbies":["Running","Volleyball"],
    "friend_list":["Tharun","Ashif","Vivek"]

},
{
    "name" : "Kabeesh",
    "e_mail" : "kabeesh@gmail.com",
    "password" : "kabeesh@123",
    "hobbies":["Cricket","Football"],
    "friend_list":["Ansari","Javith","Ajessh"]
},
{
    "name" : "Naathan",
    "e_mail" : "naathan@gmail.com",
    "password" : "naathan@123",
    "hobbies":["Cricket","Swimming"],
    "friend_list":["sabari","pravin","Safeek"]
},
{
    "name" : "Gopal",
    "e_mail" : "gopal@gmail.com",
    "password" : "gopal@123",
    "hobbies":["Cricket","Swimming"],
    "friend_list":["sabari","pravin","Safeek"]
}]
mail=input("Enter The Mail ID: ")
password=input("Enter The Password : ")
def details(detail,m_id,passwd):
    for detai in detail:
        e_id=detai["e_mail"]
        pswd=detai["password"]
        name=detai["name"]
        hobby=detai["hobbies"]
        f_list=detai["friend_list"]
        if m_id==e_id and passwd==pswd:
            detai["LoggedIn"]=True
            print(name,"|",e_id,)
            print("Your Hobbie Is :")
            for i,val in enumerate(hobby):
                print(i+1,".",val)
            print("Your Friends Are :")
            for j,nam in enumerate(f_list):
                print(j+1,".",nam)
        else:
            detai["LoggedIn"]=False
    print(detail)
details(user_Details,mail,password)