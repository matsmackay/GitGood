import numpy as np
import pandas as pd
from Classes import User, Order, Portfolio

#import market data, set index to date and transform to datetime
market_data = pd.read_csv('stockdatawide.csv')
market_data.set_index('date', inplace = True)
market_data.index = pd.to_datetime(market_data.index)

#Set the start date to the first date we have market data and create an empty position dataframe
date = min(market_data.index)
position = pd.DataFrame(0, index=np.arange(0), columns=market_data.columns)

# Request user details
surname = input('What is your surname?: ').upper()
name = input('What is your first name?: ').upper()

while True:
    # Create the user object
    user = User(surname, name)
    print("Your username is {}.".format(user.fullname))
    print("Your user ID is {}.".format(user.user_id))

    # request order input from the user
    while True:
        order_type = input('Do you want to buy or sell stocks? ')
        if order_type in ['buy', 'sell']:
            print("input accepted")
            break
        else:
            print('order type is not valid, please enter "buy" or "sell" ')

    while True:
        product = input("Enter the name of the stock you want to {} ".format(order_type))
        if product in market_data.columns:
            print("input accepted")
            break
        else:
            print('product is not available, please select another product that is available')

    while True:
        try:
            quantity = int(input("Enter the number of stocks you want to {} ".format(order_type)))
            break
        except:
            print('Quantity is not correct, please enter a whole number')

    product_price = market_data.loc[date, product]

    # Execute order
    order = Order(user.user_id, product, quantity, order_type, product_price, date)
    order.trade()
    print("You ordered {} ".format(order.quantity) + "stocks of {}".format(order.product) + ' on {}'.format(date)
          + ' for USD {}'.format(product_price) + ' per stock')

    # update portfolio
    ### Erik+Mats to add

    break

