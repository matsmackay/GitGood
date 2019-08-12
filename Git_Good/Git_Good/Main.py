#import numpy as np
#import pandas as pd
from Classes import User, Order

# Request user details
surname = input('What is your surname?: ').upper()
name = input('What is your first name?: ').upper()
user = User(surname, name)
print("Your username is {}.".format(user.fullname))
print("Your user ID is {}.".format(user.user_id))

#request order input from the user
product = input("Enter the name of the stock you want to buy ")
quantity = int(input("Enter the number of stocks you want to buy "))

#Execute order
order = Order(user.user_id, product, quantity)
order.trade()
print("You ordered {} ".format(order.quantity) + "stocks of {}".format(order.product))