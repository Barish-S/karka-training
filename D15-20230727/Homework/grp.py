items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},             
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
    {'name': 'Beans', 'category': 'Vegetables'},
    {'name': 'Orange', 'category': 'Fruits'},

]
def item(split):
    fruit_veg={'Fruits':[],'Vegtables':[]}
    for s in split:
        cate=s["category"]
        if cate=="Fruits":
            fruit_veg["Fruits"].append(s["name"])
        elif cate=="Vegetables":
            fruit_veg["Vegtables"].append(s["name"])
    return fruit_veg
print(item(items_list))
