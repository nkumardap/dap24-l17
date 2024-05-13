"""
INTRODUCTION

In this exercise, we will simulate the classic economic model of supply and 
demand! It will require you to use all the tools you've learned at the start
 of the quarter, from lists to classes. In this scenario, each consumer has 
 only a single willingness to pay and buys at most a single item. Each producer
 has a single cost and sells at most a single item. The hints are extensive, 
 but you'll still need to think about how to implement this!
"""

"""
EXERCISE 1

Create templates that can mimic consumers and producers. The former should 
have a willingness to pay, and the latter should have a cost.

Hint: Create a class named Consumer with a single attribute: willingness_to_pay. 
Similarly, create a class named Producer with a single attribute: cost. Both of 
these attributes should be taken as arguments and assigned to the object upon 
initialization.
"""

"""
EXERCISE 2

Create a set of 10 consumers using the market demand equation P = 10 - Q and 
10 producers using the market supply equation P = Q.

Hint: Start with the consumers. Determine the maximum and minimum demand 
values manually. Iterate over the range and calculate the corresponding 
"Price" using the equation. Create a consumer object using the price as 
willingness_to_pay and append it to a list of consumers to create an iterable 
list.

Repeat this process for the producers, but instead of willingness_to_pay, 
use the "price" as the cost.
"""
"""
EXERCISE 3

Create a function to estimate the quantity demanded given a price and a list 
of consumer objects. Create another function to estimate the quantity supplied g
iven a price and a list of producer objects.

Hint: The quantity_demanded function should iterate over the set of consumers. 
If the consumer's willingness to pay exceeds the price, increase the q
uantity_demanded counter. Return this counter. The quantity_supplied 
function is similar.
"""

"""
EXERCISE 4

Find the equilibrium price and quantity.

Hint: Recall that the equilibrium price is the price at which quantity 
supplied equals quantity demanded.

Iterate over a set of prices. Find the quantity demanded and the quantity 
supplied at each price. If the two are equal, end the loop and print the 
corresponding price and quantity.
"""