from menu_item import MenuItem

menu_item1 = MenuItem("Burger", 600)
menu_item2 = MenuItem("Pizza", 800)
menu_item3 = MenuItem("Pasta", 700)
menu_item4 = MenuItem("Salad", 500)
menu_item5 = MenuItem("Sushi", 1000)
menu_item6 = MenuItem("Steak", 1200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5, menu_item6]

index = 0

for item in menu_items:
    print(f"{index}. {item.info()}")
    index += 1

print('------------------------------')

order = int(input("Enter the number of the menu item you want to order: ")) 
selected_menu = menu_items[order]
print(f"You selected: {selected_menu.info()}")

count = int(input("Enter the quantity you want to order: "))

result = selected_menu.get_total_price(count)

print(f"Total price for {count} {selected_menu.name}(s): ${result:.2f}")