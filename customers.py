# Reflection 1:
# I would use .get() when a key might not exist because it lets me
# use a default value. I would use bracket notation when I know
# the key exists and I need its value. My rule of thumb is to use .get()
# for optional information and brackets for needed information.

# Reflection 2:
# This pattern reminds me of using sumif in Excel because it adds
# amounts based on matching groups. Python can be more useful for
# large datasets because it can easily handle many records
# and more complicated calculations and numbers.


# EXERCISE 1 

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print("EXERCISE 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2

print("\nEXERCISE 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3 

print("\nEXERCISE 3")

email = customer.get("email", "no email on file")
print("Email:", email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4 

print("\nEXERCISE 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without the .items(), the loop gave only the keys.
for key in customer:
    print(key)


# EXERCISE 5 

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", tier)
print("Discount rate:", discount_rate * 100, "%")
print("Final price: $", round(final_price, 2))


# EXERCISE 6 

print("\nEXERCISE 6")

dict1 = {"name": "Alice", "tier": "platinum"}
dict2 = {"name": "Bob", "tier": "gold"}
dict3 = {"name": "Charlie", "tier": "silver"}

customers = [dict1, dict2, dict3]

for person in customers:
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f'{person["name"]}: {tier}, '
        f"discount: ${discount_amount:.2f}"
    )


# EXERCISE 7 

print("\nEXERCISE 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")


# EXERCISE 8 

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")
