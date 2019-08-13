# import numpy as np
import pandas as pd
from Classes import User, Order

market_data = pd.read_csv('stockdatawide.csv')
position = pd.DataFrame(0, index=np.arange(0), columns=market_data.columns)

# Request user details
surname = input('What is your surname?: ').upper()
name = input('What is your first name?: ').upper()

while True:
    user = User(surname, name)
    print("Your username is {}.".format(user.fullname))
    print("Your user ID is {}.".format(user.user_id))

    # request order input from the user
    while True:
        product = input("Enter the name of the stock you want to buy ")
        if product in market_data.loc[0, :]:
            print("input accepted")
            break
        else:
            print('product is not available, please select another product that is available')

    while True:
        try:
            quantity = int(input("Enter the number of stocks you want to buy "))
            break
        except:
            print('Quantity is not correct, please enter a whole number')

    # Execute order
    order = Order(user.user_id, product, quantity)
    order.trade()
    print("You ordered {} ".format(order.quantity) + "stocks of {}".format(order.product))

    break

