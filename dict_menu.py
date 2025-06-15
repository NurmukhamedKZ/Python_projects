menu = {
    "Pizza": 12.99,
    "Burger": 8.49,
    "Sushi": 15.99,
    "Pasta": 10.50,
    "Salad": 6.75,
    "Tacos": 7.20,
    "Fried Chicken": 9.99,
    "Ice Cream": 4.50,
    "Steak": 18.90,
    "Sandwich": 5.80
}

print("---------MENU---------")
for i,j in menu.items():
    print(f"{i:14}: ${j:>05.2f}")
print("----------------------")

basket = 0

while True:
    item = input("what do you want (q = quit): ")
    if item.capitalize() in menu:
        basket += menu[item.capitalize()]
        print(f"your basket costs ${basket:.2f}")
    elif item.lower() == "q":
        break
    else:
        print("plz write smt from this menu)")
    

print(f"it'll cost you ${basket:.2f}")
    