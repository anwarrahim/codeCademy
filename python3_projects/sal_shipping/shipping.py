# task 1
weight = 4.8

# task 2
# ground shipping

if weight <= 2:
    cost_ground = weight * 1.5 + 20.00
    # print(cost_ground)
elif 2 < weight <= 6:
    cost_ground = weight * 3.00 + 20.00
    # print(cost_ground)
elif 2 < weight <= 10:
    cost_ground = weight * 4.00 + 20.00
    # print(cost_ground)
elif 10 < weight:
    cost_ground = weight * 4.75 + 20.00

# Task 3 (test the code)
print(cost_ground)

# Ground Shipping premium cost
# Task 4
cost_ground_premium = 125.00

# Task 5
# print code
print("premium cost ground:" + " " + str(cost_ground_premium))

# Drone Shipping
# Task 6
if 2 >= weight:
    cost_ground_shipping = weight * 4.50 + 0.00
elif 2 < weight <= 6:
    cost_ground_shipping = weight * 9.00 + 0.00
elif 6 < weight <= 10:
    cost_ground_shipping = weight * 12.00 + 0.00
elif 10 < weight:
    cost_ground_shipping = weight * 14.25 + 0.00

print(cost_ground_shipping)

# Task 7
# put the value to check is it working correctly













