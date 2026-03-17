import sys

def main():
    # Initialize inventory as simple dictionary for command-line items
    inventory = {}
    
    # Process command-line arguments if provided
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                if ':' in arg:
                    item_name, qty = arg.split(':')
                    quantity = int(qty)
                    inventory[item_name] = quantity
                else:
                    print(f"Invalid format: '{arg}' (use 'item:quantity')")
            except (ValueError, IndexError) as e:
                print(f"Error parsing '{arg}': {e}")
    else:
        # Default inventory if no arguments provided
        inventory = {"sword": 1, "potion": 5, "shield": 2, "armor": 3, "helmet": 1}
    
    # Display analysis
    print_inventory_analysis(inventory)

def print_inventory_analysis(inventory):
    """Print complete inventory analysis"""
    if not inventory:
        print("Inventory is empty!")
        return
    
    total_items = sum(inventory.values())
    unique_items = len(inventory)
    
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    
    # Current Inventory
    print("=== Current Inventory ===")
    for item, quantity in inventory.items():
        percentage = (quantity / total_items) * 100
        print(f"{item}: {quantity} units ({percentage:.1f}%)")
    
    # Inventory Statistics
    print("=== Inventory Statistics ===")
    quantities = list(inventory.values())
    most_abundant_qty = max(quantities)
    least_abundant_qty = min(quantities)
    
    most_items = [item for item, qty in inventory.items() if qty == most_abundant_qty]
    least_items = [item for item, qty in inventory.items() if qty == least_abundant_qty]
    
    print(f"Most abundant: {', '.join(most_items)} ({most_abundant_qty} units)")
    print(f"Least abundant: {', '.join(least_items)} ({least_abundant_qty} unit)" if least_abundant_qty == 1 else f"Least abundant: {', '.join(least_items)} ({least_abundant_qty} units)")
    
    # Item Categories
    print("=== Item Categories ===")
    moderate = {}
    scarce = {}
    
    for item, qty in inventory.items():
        if qty >= 5:
            moderate[item] = qty
        else:
            scarce[item] = qty
    
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")
    
    # Management Suggestions
    print("=== Management Suggestions ===")
    restock_needed = [item for item, qty in inventory.items() if qty < 2]
    if restock_needed:
        print(f"Restock needed: {', '.join(restock_needed)}")
    else:
        print("All items stocked adequately")
    
    # Dictionary Properties Demo
    print("=== Dictionary Properties Demo ===")
    keys_list = list(inventory.keys())
    values_list = list(inventory.values())
    
    print(f"Dictionary keys: {', '.join(keys_list)}")
    print(f"Dictionary values: {', '.join(map(str, values_list))}")
    
    # Membership test with first item
    if inventory:
        test_item = list(inventory.keys())[0]
        exists = test_item in inventory
        print(f"Sample lookup- '{test_item}' in inventory: {exists}")

if __name__ == "__main__":
    main()