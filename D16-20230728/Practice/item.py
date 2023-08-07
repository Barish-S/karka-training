items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},             
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
    {'name': 'Beans', 'category': 'Vegetables'},
    {'name': 'Orange', 'category': 'Fruits'},
    {'name': 'Jasmine', 'category': 'Flowers'},
    {'name': 'Rose', 'category': 'Flowers'},
    {'name': 'Lavender', 'category': 'Flowers'},

]
def item(split):
    a={}
    for i in split:
        if i["category"] in a:
            a[i["category"]].append(i["name"])
        else:
            a[i["category"]]=[i["name"]]
    return a
print(item(items_list))