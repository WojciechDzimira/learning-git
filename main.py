shoping_list = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
    "cukiernia": ["krówki", "lizaki"], 
     }
item_counter = 0

for shop, items in shoping_list.items():
    print(f"Idę do {shop.capitalize()} i kupuje tam {[item.capitalize() for item in items]}.") 
    item_counter += len(items) 

print(f"w sumie kupię: {item_counter} produktów.")

print("cześć, mentorze :)")