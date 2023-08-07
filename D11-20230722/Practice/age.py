names=[{"name":"Barish",
        "age":23},
       {"name":"Saheen",
        "age":21},
        {"name":"Nuvaf",
        "age":22},]
total=0
for n in names:
    total=n["age"]+total
print(total)