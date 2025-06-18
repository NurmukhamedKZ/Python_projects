class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def total(self):
        answer = [i.name for i in self.items]
        
        return sum(item.price for item in self.items)

# Example usage
p1 = Product("Book", 12.99)
p2 = Product("Pen", 1.99)


cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2)

cart.total()

