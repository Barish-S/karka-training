user_Details = [{
    "name" : "saravana",
    "e_mail" : "saravana@gmail.com",
    "password" : "saravan@123",
    "hobbies":["Cricket","Volleyball"],
    "friend_list":["Saheen","Ashif","Safeek"]
},
{
    "name" : "benish",
    "e_mail" : "benish@gmail.com",
    "password" : "benish@123",
    "hobbies":["Running","Volleyball"],
    "friend_list":["Tharun","Ashif","Vivek"]

},
{
    "name" : "kabeesh",
    "e_mail" : "kabeesh@gmail.com",
    "password" : "kabeesh@123",
    "hobbies":["Cricket","Football"],
    "friend_list":["Ansari","Javith","Ajessh"]
},
{
    "name" : "naathan",
    "e_mail" : "naathan@gmail.com",
    "password" : "naathan@123",
    "hobbies":["Cricket","Swimming"],
    "friend_list":["sabari","pravin","Safeek"]
},
{
    "name" : "naathan",
    "e_mail" : "naathan@gmail.com",
    "password" : "naathan@123",
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
            print(name,"|",e_id,"Your Hobby Is: ",hobby,"You Are Friends Are : ",f_list)
details(user_Details,mail,password)