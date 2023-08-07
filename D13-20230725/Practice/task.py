user=input("Enter The Hobbies : ")
name=[]
my_details=[
           {"name":"Barish" ,
            "place":"Madhavalayam",
            "Hobbies":["Cricket","Listening Music","Cooking"]
            },
            {"name":"Gokul",
            "place":"Arumanalloor",
            "Hobbies":["Cricket","Football","Dancing"]},            
            {
            "name":"Abishek",
            "place":"Krishnakovil",
            "Hobbies":["Tattoing","Football","Cooking"]
            },
            {
            "name":"Siva",
            "place":"Mandaymarket",
            "Hobbies":["Running","Swimming","Cricket"]
            },
            {
            "name":"Jason",
            "place":"Pambanvilai",
            "Hobbies":["Chess","Cricket","Football"]
            },
            {
            "name":"Manimala",
            "place":"Vadasey",
            "Hobbies":["Cooking","Drawing","Painting"]
            },
            {
            "name":"Mahalakshmi",
            "place":"Pazhavoor",
            "Hobbies":["Cooking","Listening Music","Mehandi"]
            },
            {
            "name":"Nancy",
            "place":"Mandaymarket",
            "Hobbies":["Drawing","Cooking","KoKo"]
            },
            {"name":"Abarna",
            "place":"Therisanankopu",
            "Hobbies":["Cooking","Drawing","Listening Music"]}
]
my_details.append({"name":"Saheen" ,
            "place":"Madhavalayam",
            "Hobbies":["Cricket","Listening Music","Cooking"]})
for n in my_details:
    for hob in n["Hobbies"]:
        if user==hob:
           name.append(n["name"])
print(name)