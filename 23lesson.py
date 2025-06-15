foods = []
prices = []

while True:
    food = input("enter a food(q to quit): ")
    if food.lower() == "q":
        break
    foods.append(food)
    price = float(input(f"enter a {food}'s price: "))
    prices.append(price)

print("   MENU   ")
for i in range(len(foods)):
    print(f"{foods[i]} ----- ${prices[i]}")
