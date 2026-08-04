# Initialize the dictionary with initial fruit prices
fruit_price  = {
    "Apple": 1500,
    "Bannana": 1000,
    "Orage": 1200
    }
print("Inventory Dictionary 1:")
print(fruit_price)
total_items = len(fruit_price)
print("Total number of items in inventory 1:", total_items)
print("-" *50)

# Update banana price and completely remove apple
fruit_price["Bannana"]=1100
del fruit_price["Apple"]
print("Inventory Dictionary 2:")
print(fruit_price)
total_items = len(fruit_price)
print("Total number of items in inventory 2:", total_items)
print("-" *50)

# Add new items (Mango and re-adding Apple with a new price)
fruit_price["Mango"]=2000
fruit_price["Bannana"]=1400
print("Inventory Dictionary 3:")
print(fruit_price)
total_items = len(fruit_price)
print("Total number of items in inventory 3:", total_items)
print("-" *50)

# Print the final inventory and the total number of items
fruit_price["Apple"]=1500
print("Final Inventory Dictionary:")
print(fruit_price)
total_items = len(fruit_price)
print("Final total number of items in inventory:", total_items)
