#zadanie: pierwsze Samodzielne commity


shoping_list = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"], 
    "monopolowy": ["wino"]
    }
item_counter = 0

for shop, items in shoping_list.items():
    print(f"Idę do {shop.capitalize()} i kupuje tam {[item.capitalize() for item in items]}.") #.join zamienione na capitalize()
    item_counter += len(items) 

print(f"w sumie kupię: {item_counter} produktów.")
print("halo to ja")
