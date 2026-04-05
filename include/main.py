from core_logic import CafeManager
import sys


def display_menu(manager: CafeManager):
    print("\n" + "="*50)
    print("                  SMART CAFE MENU")
    print("="*50)

    categories = manager.get_menu_by_category()
    for category, items in categories.items():
        print(f"\n{category.upper()}:")
        for item in items:
            status = "✅" if item.available else "❌"
            print(f"  {status} {item.id:2d}. {item.name:<20} Rs. {item.price:6.2f}")
    print("="*50)


def take_order(manager: CafeManager):
    display_menu(manager)

    print("\nEnter items for order (type 'done' when finished):")
    order_list = []

    while True:
        try:
            item_input = input("\nEnter Item ID (or 'done'): ").strip()
            if item_input.lower() == 'done':
                break

            item_id = int(item_input)
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be positive!")
                continue

            order_list.append({"item_id": item_id, "quantity": quantity})

        except ValueError:
            print("Invalid input! Please enter numbers.")

    if not order_list:
        print("No items selected.")
        return

    try:
        order = manager.create_order(order_list)
        print("\n" + "✓" * 20)
        print("ORDER PLACED SUCCESSFULLY!")
        print("✓" * 20)
        print(f"Order ID     : {order['order_id']}")
        print(f"Total Amount : Rs. {order['total']:.2f}")
        print(f"Time         : {order['timestamp'][:19]}")
        print("Thank you for ordering at SmartCafe! ☕")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    manager = CafeManager()

    # Sample data if menu is empty
    if not manager.get_menu():
        print("Initializing sample menu...")
        manager.add_menu_item("Espresso", 250, "Beverages")
        manager.add_menu_item("Cappuccino", 320, "Beverages")
        manager.add_menu_item("Cheese Sandwich", 280, "Food")
        manager.add_menu_item("Chicken Shawarma", 450, "Food")
        manager.add_menu_item("Chocolate Cake", 180, "Desserts")
        manager.add_menu_item("French Fries", 220, "Snacks")

    while True:
        print("\n" + "="*50)
        print("                  SMART CAFE")
        print("="*50)
        print("1. Show Menu")
        print("2. Take New Order")
        print("3. View All Orders")
        print("4. Show Revenue")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            display_menu(manager)
        elif choice == "2":
            take_order(manager)
        elif choice == "3":
            orders = manager.get_all_orders()
            if orders:
                print(f"\nTotal Orders: {len(orders)}")
                for order in orders[-5:]:  # Show last 5 orders
                    print(f"Order #{order['order_id']} | Rs. {order['total']:.2f} | {order['timestamp'][:10]}")
            else:
                print("No orders yet.")
        elif choice == "4":
            print(f"\nTotal Revenue: Rs. {manager.get_total_revenue():.2f}")
        elif choice == "5":
            print("Thank you for using SmartCafe! Goodbye 👋")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")