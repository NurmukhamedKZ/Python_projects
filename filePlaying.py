import json

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


file_path = "stuff/text1.json"


try:
    with open(file_path, "w") as f:
        json.dump(menu, f, indent=4)
            
except FileExistsError:
    print(f"'{file_path}' already exists")