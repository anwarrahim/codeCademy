# this is the file
# Your code below:
# Task 1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "olives", "anchovies", "mushrooms"]
# Task 2
prices = [2, 6, 1, 3, 2, 7, 2]

# Task 3
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# Task 4
num_pizzas = len(toppings)
# Task 5
print("we sell " + str(num_pizzas) + " different kinds of pizza!")

# Task 6
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"],
                    [2, "mushrooms"]]

# Task 7
print(pizza_and_prices)

# sorting and Slicing Pizzas
# task 8
pizza_and_prices = pizza_and_prices.sort()

# Task 9
cheapest_price = pizza_and_prices[0]
print(cheapest_price)

# Task 10
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Task 11
priciest_pizza.pop()
print(priciest_pizza)

# Task 12
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Task 13
three_cheapest = pizza_and_prices[:3]

# Task 14
print(three_cheapest)
