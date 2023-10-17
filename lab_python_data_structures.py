# -*- coding: utf-8 -*-
"""lab-python-data-structures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TsnbhWeHVUrnJAWdJ7KSEtkOVRPVtB_r

# Lab | Data Structures

## Exercise: Managing Customer Orders

As part of a business venture, you are starting an online store that sells various products. To ensure smooth operations, you need to develop a program that manages customer orders and inventory.

Follow the steps below to complete the exercise:

1. Define a list called `products` that contains the following items: "t-shirt", "mug", "hat", "book", "keychain".

2. Create an empty dictionary called `inventory`.

3. Ask the user to input the quantity of each product available in the inventory. Use the product names from the `products` list as keys in the `inventory` dictionary and assign the respective quantities as values.

4. Create an empty set called `customer_orders`.

5. Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of "t-shirt", "mug", "hat", "book" or "keychain". Add each product name to the `customer_orders` set.

6. Print the products in the `customer_orders` set.

7. Calculate the following order statistics:
   - Total Products Ordered: The total number of products in the `customer_orders` set.
   - Percentage of Products Ordered: The percentage of products ordered compared to the total available products.
   
   Store these statistics in a tuple called `order_status`.

8. Print the order statistics using the following format:
   ```
   Order Statistics:
   Total Products Ordered: <total_products_ordered>
   Percentage of Products Ordered: <percentage_ordered>%
   ```

9. Update the inventory by subtracting 1 from the quantity of each product. Modify the `inventory` dictionary accordingly.

10. Print the updated inventory, displaying the quantity of each product on separate lines.

Solve the exercise by implementing the steps using the Python concepts of lists, dictionaries, sets, and basic input/output operations.
"""

# Define a list called products that contains the following items: "t-shirt", "mug", "hat", "book", "keychain".

products = ("t-shirt", "mug", "hat", "book", "keychain")

# Create an empty dictionary called inventory.

inventory = {}

# Ask the user to input the quantity of each product available in the inventory. Use the product names from the products list as keys in the inventory dictionary and assign the respective quantities as values.

products = ("t-shirt", "mug", "hat", "book", "keychain")
inventory = {}

for product in products:
    quantity = int(input(f"Enter the quantity of {product}: "))
    inventory[product] = quantity

print("Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

# Create an empty set called customer_orders.

customer_orders = set()

# Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of "t-shirt", "mug", "hat", "book" or "keychain". Add each product name to the customer_orders set.

products = ["t-shirt", "mug", "hat", "book", "keychain"]

customer_orders = set()

for _ in range(3):
    product_name = input("Enter a product name you want to order: ")

    if product_name in products:
        customer_orders.add(product_name)
    else:
        print("Invalid product name. Please choose from the available products.")

print("Customer's Order:")
for product in customer_orders:
    print(product)

# Print the products in the customer_orders set.

print("Products in the Customer's Order:")
for product in customer_orders:
    print(product)

# Total Products Ordered: The total number of products in the customer_orders set.

total_products_ordered = len(customer_orders)

print("Total Products Ordered:", total_products_ordered)

# Percentage of Products Ordered: The percentage of products ordered compared to the total available products.

total_products_ordered = len(customer_orders)
print("Total of products orded", total_products_ordered)
total_available_products = sum(inventory.values())
print('Total products: ',total_available_products)
percentage_ordered = (total_products_ordered / total_available_products) * 100

print("Percentage of Products Ordered:", percentage_ordered, "%")

#store these statistics in a tuple called order_status.

order_status = (total_products_ordered, percentage_ordered)
print(order_status)

print(inventory)

for product in customer_orders:
    if product in inventory and inventory[product] > 0:
        inventory[product] -= 1
    else:
        print(f"message: None {product} available in the inventory.")

print("Updated Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")



"""Fred, the last i could´t do it. I even try to search in internet but still confuse to me. I will spend mopre time trying to understand it. I am sorry :("""
