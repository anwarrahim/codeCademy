# new project Receipts for Lovely Loveseats
# step 1
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 
30 inches deep. Red or white. """

# step 2
lovely_loveseat_price = 254.00

# step 3
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 
inches deep. Black. """

# step 4
stylish_settee_price = 180.50

# step 5
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

# step 6
luxurious_lamp_price = 52.15

# step 7
sales_tax = 0.088

# step 8
# our first customer
customer_one_total = 0

# step 9
customer_one_itemization = ""

# step 10
customer_one_total += lovely_loveseat_price

# step 11
customer_one_itemization += lovely_loveseat_description

# step 12
customer_one_total += luxurious_lamp_price

# step 13
customer_one_itemization += luxurious_lamp_description

# step 14
customer_one_tax = customer_one_total * sales_tax

# step 15
customer_one_total += customer_one_tax

# step 16
print("Customer One Items:")

# step 17
print(customer_one_itemization)

# step 18
print("Customer One Total:")

# step 19
print(customer_one_total)
