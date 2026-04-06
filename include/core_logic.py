from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional
import json
from pathlib import Path


@dataclass
class MenuItem:
    id: int
    name: str
    price: float
    category: str
    available: bool = True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "available": self.available,
        }


@dataclass
class OrderItem:
    menu_item: MenuItem
    quantity: int

    def subtotal(self) -> float:
        return self.menu_item.price * self.quantity


class CafeManager:
    def __init__(self, data_file: str = "Smart Cafe/database/cafe_data.json"):
        self.menu: List[MenuItem] = []
        self.orders: List[Dict] = []
        self.data_file = Path(data_file)
        self._load_data()

    def _load_data(self):
        """Load menu and orders from JSON file if exists"""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.menu = [MenuItem(**item) for item in data.get("menu", [])]
                    self.orders = data.get("orders", [])
            except Exception:
                print("Warning: Could not load data. Starting fresh.")

    def _save_data(self):
        """Save current state to JSON file"""
        data = {
            "menu": [item.to_dict() for item in self.menu],
            "orders": self.orders
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    # ==================== MENU MANAGEMENT ====================
    def add_menu_item(self, name: str, price: float, category: str) -> MenuItem:
        item_id = max([item.id for item in self.menu], default=0) + 1
        item = MenuItem(id=item_id, name=name, price=price, category=category)
        self.menu.append(item)
        self._save_data()
        return item

    def get_menu(self, category: Optional[str] = None) -> List[MenuItem]:
        if category:
            return [item for item in self.menu if item.category.lower() == category.lower()]
        return self.menu

    def update_availability(self, item_id: int, available: bool):
        for item in self.menu:
            if item.id == item_id:
                item.available = available
                self._save_data()
                return True
        return False

    # ==================== ORDER MANAGEMENT ====================
    def create_order(self, items: List[dict]) -> dict:
        """items format: [{"item_id": 1, "quantity": 2}, ...]"""
        order_items: List[OrderItem] = []
        total = 0.0

        for entry in items:
            item_id = entry["item_id"]
            quantity = entry["quantity"]

            menu_item = next((item for item in self.menu if item.id == item_id), None)
            if not menu_item or not menu_item.available:
                raise ValueError(f"Item ID {item_id} is not available.")

            order_item = OrderItem(menu_item=menu_item, quantity=quantity)
            order_items.append(order_item)
            total += order_item.subtotal()

        order = {
            "order_id": len(self.orders) + 1,
            "timestamp": datetime.now().isoformat(),
            "items": [ {
                "name": oi.menu_item.name,
                "quantity": oi.quantity,
                "price": oi.menu_item.price,
                "subtotal": oi.subtotal()
            } for oi in order_items ],
            "total": round(total, 2)
        }

        self.orders.append(order)
        self._save_data()
        return order

    def get_all_orders(self) -> List[dict]:
        return self.orders

    def get_order(self, order_id: int) -> Optional[dict]:
        return next((order for order in self.orders if order["order_id"] == order_id), None)

    # ==================== UTILITIES ====================
    def get_total_revenue(self) -> float:
        return round(sum(order["total"] for order in self.orders), 2)

    def get_menu_by_category(self) -> Dict[str, List[MenuItem]]:
        categories: Dict[str, List[MenuItem]] = {}
        for item in self.menu:
            categories.setdefault(item.category, []).append(item)
        return categories