from dataclasses import dataclass

# Menu item using dataclass
@dataclass
class MenuItem:
    name: str
    price: float

# Order class using dataclass
@dataclass
class Order:
    customer_name: str
    items: list  # List of MenuItem

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

# Restaurant class managing menu and orders
class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)
        print(f"Added {name} (₹{price}) to menu.")

    def show_menu(self):
        if not self.menu:
            print("Menu is empty.\n")
            return
        print("\n--- MENU ---")
        for i, item in enumerate(self.menu):
            print(f"{i+1}. {item.name} - ₹{item.price}")
        print()

    def take_order(self):
        if not self.menu:
            print("Menu is empty. Add items first.\n")
            return

        customer_name = input("Enter customer name: ")
        self.show_menu()
        item_numbers = input("Enter item numbers): ")
        item_indices = item_numbers.split(",")

        ordered_items = []
        for idx in item_indices:
            idx = idx.strip()
            if idx.isdigit():
                idx = int(idx) - 1
                if 0 <= idx < len(self.menu):
                    ordered_items.append(self.menu[idx])
                else:
                    print(f"Item number {idx+1} is not in the menu.")
            else:
                print(f"'{idx}' is not a valid number.")

        if ordered_items:
            order = Order(customer_name, ordered_items)
            self.orders.append(order)
            print(f"Order placed for {customer_name}. Total = ₹{order.total_price()}\n")
        else:
            print("No valid items selected. Order not placed.\n")

    def show_all_orders(self):
        if not self.orders:
            print("No orders placed yet.\n")
            return

        print("\n--- ALL ORDERS ---")
        for i, order in enumerate(self.orders):
            item_names = ", ".join(item.name for item in order.items)
            print(f"{i+1}. {order.customer_name} ordered: {item_names} | Total: ₹{order.total_price()}")
        print()

# Main program loop
def main():
    restaurant = Restaurant()

    while True:
        print("=== Restaurant Menu ===")
        print("1. Add Menu Item")
        print("2. Show Menu")
        print("3. Take Order")
        print("4. Show All Orders")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter item name: ")
            price_input = input("Enter item price: ")
            if price_input.replace('.', '', 1).isdigit():
                price = float(price_input)
                restaurant.add_menu_item(name, price)
            else:
                print("Invalid price. Please enter a number.\n")

        elif choice == "2":
            restaurant.show_menu()

        elif choice == "3":
            restaurant.take_order()

        elif choice == "4":
            restaurant.show_all_orders()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
