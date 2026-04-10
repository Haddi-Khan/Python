class Cart:
    def __init__(self):
        self.items = {}   
        
    def add_item(self, item, price):
        self.items[item] = price
        print(f" {item} added with price {price}")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f" {item} removed from cart")
        else:
            print(f"{item} not found in cart")

    def get_total(self):
        total = sum(self.items.values())
        print(f" Total amount = {total}")
        return total

    def show_cart(self):
        if self.items:
            print("    Your Cart    ")
            for item, price in self.items.items():
                print(f"{item} : {price}")
        else:
            print("Your cart is empty.")

cart = Cart()
cart.add_item("Shirt", 1200)
cart.add_item("Shoes", 3000)
cart.show_cart()
cart.get_total()
cart.remove_item("Shirt")
cart.show_cart()
cart.get_total()