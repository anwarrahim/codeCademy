
# Len's Slice
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.
Make Some Pizzas
1.
To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:

"pepperoni"
"pineapple"
"cheese"
"sausage"
"olives"
"anchovies"
"mushrooms"


2.
To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:

2
6
1
3
2
7
2


3.
Your boss wants you to do some research on $2 slices.

Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.

4.
Find the length of the toppings list and store it in a variable called num_pizzas.



5.
Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.


6.
Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.

Each sublist in pizza_and_prices should have one pizza topping and an associated price.

Price	Topping
2	"pepperoni"
6	"pineapple"
1	"cheese"
3	"sausage"
2	"olives"
7	"anchovies"
2	"mushrooms"

For this new list make sure the prices come before the topping name like so:

Note: You don’t need to use your original toppings and prices lists in this exercise. Create a new two-dimensional list from scratch.


7.
Print pizza_and_prices.

Does it look the way you expect?


Sorting and Slicing Pizzas
8.
Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).

9.
Store the first element of pizza_and_prices in a variable called cheapest_pizza.



10.
A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.


11.
It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.



12.
Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:

                                [2.5, "peppers"]
Add the new peppers pizza topping to our list pizza_and_prices.

Note: Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!



13.
Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.


14.
Great job! The mice are very pleased and will be leaving you a 5-star review.

Print the three_cheapest list.