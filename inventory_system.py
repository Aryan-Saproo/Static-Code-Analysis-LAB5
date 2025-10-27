"""
Inventory Management System
---------------------------
This module manages a simple inventory system that allows adding, removing, 
loading, and saving stock data with logging and safety improvements.
"""

import json
from datetime import datetime

# Inventory data storage
stock_data = {}


def add_item(item: str, qty: int = 0, logs=None):
    """Add an item with a specified quantity to the inventory."""
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types: item must be str and qty must be int.")
        return

    if logs is None:
        logs = []

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int):
    """Remove a quantity of an item from the inventory."""
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types.")
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory.")


def get_qty(item: str) -> int:
    """Return the quantity of the specified item."""
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        print("Inventory data loaded successfully.")
    except FileNotFoundError:
        print("No existing inventory file found. Starting fresh.")


def save_data(file: str = "inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    print("Inventory data saved successfully.")


def print_data():
    """Display all items and their quantities."""
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> list:
    """Return a list of items with stock below a threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function demonstrating inventory operations."""
    load_data()
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())
    print_data()
    save_data()


if __name__ == "__main__":
    main()
