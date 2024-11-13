Here's a simple inventory management system for a grocery store in Python:


class GroceryStore:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity, price, category):
        self.inventory[name] = {
            "quantity": quantity,
            "price": price,
            "category": category
        }
        print(f"Product '{name}' added successfully.")

    def remove_product(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"Product '{name}' removed successfully.")
        else:
            print(f"Product '{name}' not found.")

    def update_quantity(self, name, quantity):
        if name in self.inventory:
            self.inventory[name]["quantity"] = quantity
            print(f"Quantity of '{name}' updated successfully.")
        else:
            print(f"Product '{name}' not found.")

    def update_price(self, name, price):
        if name in self.inventory:
            self.inventory[name]["price"] = price
            print(f"Price of '{name}' updated successfully.")
        else:
            print(f"Product '{name}' not found.")

    def display_inventory(self):
        print("Current Inventory:")
        for product, details in self.inventory.items():
            print(f"Product: {product}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}, Category: {details['category']}")

    def search_product(self, name):
        if name in self.inventory:
            print(f"Product '{name}' found. Quantity: {self.inventory[name]['quantity']}, Price: ${self.inventory[name]['price']:.2f}, Category: {self.inventory[name]['category']}")
        else:
            print(f"Product '{name}' not found.")

    def reorder_products(self):
        reorder_list = [product for product, details in self.inventory.items() if details["quantity"] <= 5]
        print("Reorder List:")
        for product in reorder_list:
            print(f"Product: {product}, Quantity: {self.inventory[product]['quantity']}, Price: ${self.inventory[product]['price']:.2f}, Category: {self.inventory[product]['category']}")

def main():
    store = GroceryStore()

    while True:
        print("\nGrocery Store Inventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. Update Price")
        print("5. Display Inventory")
        print("6. Search Product")
        print("7. Reorder Products")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            category = input("Enter category (e.g., Produce, Dairy, Meat): ")
            store.add_product(name, quantity, price, category)
        elif choice == "2":
            name = input("Enter product name: ")
            store.remove_product(name)
        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input("Enter new quantity: "))
            store.update_quantity(name, quantity)
        elif choice == "4":
            name = input("Enter product name: ")
            price = float(input("Enter new price: "))
            store.update_price(name, price)
        elif choice == "5":
            store.display_inventory()
        elif choice == "6":
            name = input("Enter product name: ")
            store.search_product(name)
        elif choice == "7":
            store.reorder_products()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main
 






