from core_logic import CafeManager
import sys


def display_menu(manager: CafeManager):
    print("\n" + "="*60)
    print("                  SMART CAFE MENU")
    print("="*60)

    categories = manager.get_menu_by_category()
    for category, items in categories.items():
        print(f"\n{category.upper()}:")
        for item in items:
            status = "Available" if item.available else "Unavailable"
            print(f"  {item.id:2d}. {item.name:<25} Rs. {item.price:6.2f}  [{status}]")
    print("="*60)


def build_order(manager: CafeManager):
    """Interactive order builder with remove option"""
    current_order = []  # list of {"item_id": , "quantity": }

    print("\n" + "="*50)
    print("              BUILD YOUR ORDER")
    print("="*50)

    while True:
        display_menu(manager)
        print("\nCurrent Order:")
        if not current_order:
            print("   (No items yet)")
        else:
            subtotal = 0
            for idx, item in enumerate(current_order, 1):
                menu_item = next((m for m in manager.menu if m.id == item["item_id"]), None)
                if menu_item:
                    item_sub = menu_item.price * item["quantity"]
                    subtotal += item_sub
                    print(f"  {idx}. {menu_item.name} x{item['quantity']} = Rs. {item_sub:.2f}")
            print(f"   Subtotal so far: Rs. {subtotal:.2f}")

        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item from Order")
        print("3. Place Order")
        print("4. Cancel Order")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            try:
                item_id = int(input("Enter Item ID: "))
                quantity = int(input("Enter Quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
                current_order.append({"item_id": item_id, "quantity": quantity})
                print("Item added to order.")
            except ValueError:
                print("Invalid input!")

        elif choice == "2":
            if not current_order:
                print("Order is empty!")
                continue
            try:
                idx = int(input("Enter item number to remove: ")) - 1
                if 0 <= idx < len(current_order):
                    removed = current_order.pop(idx)
                    menu_item = next((m for m in manager.menu if m.id == removed["item_id"]), None)
                    print(f"Removed: {menu_item.name if menu_item else 'Item'}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Invalid input!")

        elif choice == "3":
            if not current_order:
                print("Cannot place empty order!")
                continue
            try:
                order = manager.create_order(current_order)
                print("\n" + "✓" * 25)
                print("ORDER PLACED SUCCESSFULLY!")
                print("✓" * 25)
                print(f"Order ID     : #{order['order_id']}")
                print(f"Subtotal     : Rs. {order['subtotal']:.2f}")
                print(f"Tax (5%)     : Rs. {order['tax']:.2f}")
                print(f"Total Amount : Rs. {order['total']:.2f}")
                print(f"Time         : {order['timestamp'][:19]}")
                print("\nThank you for ordering at SmartCafe! ☕")
                return
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Order cancelled.")
            return
        else:
            print("Invalid choice!")


def admin_menu(manager: CafeManager):
    while True:
        print("\n" + "="*50)
        print("              ADMIN / STAFF PANEL")
        print("="*50)
        print("1. Show Full Menu")
        print("2. Add New Menu Item")
        print("3. Update Menu Item")
        print("4. Remove Menu Item")
        print("5. Toggle Item Availability")
        print("6. View All Orders")
        print("7. Show Total Revenue")
        print("8. Back to Main Menu")

        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "1":
            display_menu(manager)

        elif choice == "2":
            name = input("Item Name: ").strip()
            try:
                price = float(input("Price (Rs.): "))
                category = input("Category: ").strip()
                item = manager.add_menu_item(name, price, category)
                print(f"Added: {item.name} (ID: {item.id})")
            except ValueError:
                print("Invalid price!")

        elif choice == "3":
            try:
                item_id = int(input("Enter Item ID to update: "))
                name = input("New Name (press Enter to keep same): ").strip()
                price_input = input("New Price (press Enter to keep same): ").strip()
                category = input("New Category (press Enter to keep same): ").strip()

                price = float(price_input) if price_input else None
                success = manager.update_menu_item(
                    item_id,
                    name if name else None,
                    price,
                    category if category else None
                )
                print("Updated successfully!" if success else "Item not found!")
            except ValueError:
                print("Invalid input!")

        elif choice == "4":
            try:
                item_id = int(input("Enter Item ID to remove: "))
                if manager.remove_menu_item(item_id):
                    print("Item removed successfully!")
                else:
                    print("Item not found!")
            except ValueError:
                print("Invalid ID!")

        elif choice == "5":
            try:
                item_id = int(input("Enter Item ID: "))
                status = input("Available? (y/n): ").strip().lower()
                available = status == 'y'
                if manager.update_availability(item_id, available):
                    print(f"Item availability updated to {'Available' if available else 'Unavailable'}")
                else:
                    print("Item not found!")
            except ValueError:
                print("Invalid input!")

        elif choice == "6":
            orders = manager.get_all_orders()
            if orders:
                print(f"\nTotal Orders: {len(orders)}")
                for order in orders[-10:]:  # Last 10 orders
                    print(f"#{order['order_id']:3d} | Rs. {order['total']:7.2f} | {order['timestamp'][:16]}")
            else:
                print("No orders yet.")

        elif choice == "7":
            print(f"\nTotal Revenue: Rs. {manager.get_total_revenue():.2f}")

        elif choice == "8":
            break
        else:
            print("Invalid choice!")


def main():
    manager = CafeManager()

    # Initialize sample data if menu is empty
    if not manager.get_menu():
        print("Initializing sample menu...")
        manager.add_menu_item("Espresso", 250, "Beverages")
        manager.add_menu_item("Cappuccino", 320, "Beverages")
        manager.add_menu_item("Latte", 280, "Beverages")
        manager.add_menu_item("Cheese Sandwich", 280, "Food")
        manager.add_menu_item("Chicken Shawarma", 450, "Food")
        manager.add_menu_item("French Fries", 220, "Snacks")
        manager.add_menu_item("Chocolate Cake", 180, "Desserts")

    while True:
        print("\n" + "="*60)
        print("                    SMART CAFE")
        print("="*60)
        print("1. Customer Mode - Place Order")
        print("2. Staff/Admin Mode")
        print("3. Show Menu")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            build_order(manager)
        elif choice == "2":
            admin_menu(manager)
        elif choice == "3":
            display_menu(manager)
        elif choice == "4":
            print("Thank you for using SmartCafe! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")