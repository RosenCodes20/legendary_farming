items_dict = {"shards":0,"fragments":0,"motes":0}
is_obtained = False

while not is_obtained:
    current_items = input().split()
    for index in range(0,len(current_items),2):
        current_value = int(current_items[index])
        current_key = current_items[index+1].lower()
        if current_key not in items_dict.keys():
            items_dict[current_key] = 0
        items_dict[current_key] += current_value

        if items_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            is_obtained = True
            items_dict["shards"] -= 250

        elif items_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            is_obtained = True
            items_dict["fragments"] -= 250

        elif items_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            is_obtained = True
            items_dict["motes"] -= 250
        if is_obtained:
            break

for item,quantity in items_dict.items():
    print(f"{item}: {quantity}")

