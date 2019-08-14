import numpy as np
import pandas as pd
from Git_Good.Git_Good.Classes import User, Order, Portfolio, UserExperience

# import market data, set index to date and transform to datetime
market_data = pd.read_csv('stockdatawide.csv')
market_data.set_index('date', inplace=True)
market_data.index = pd.to_datetime(market_data.index)

# Set the start date to the first date we have market data and create an empty position dataframe
counter = 0
position = pd.DataFrame(0, index=np.arange(0), columns=market_data.columns)

# Request user details
surname = input('What is your surname?: ').upper()
name = input('What is your first name?: ').upper()
user = User(surname, name)
user_exp = UserExperience(User.user_id)
portfolio_user = Portfolio(user.user_id, position)

while True:
    # Create the user object
    date = market_data.index[counter]
    user_exp.call_assistant(user.fullname, counter)

    if len(portfolio_user.position.index) == 0:
        print("Your portfolio is currently empty")
    else:
        print("Your portfolio is currently as follows:")
        print(portfolio_user.get_positions())

    trade_indicator = user_exp.trade_indicator_func(date)

    if trade_indicator == 'yes':
        while True:
            # request order input from the user
            order_type = user_exp.order_type_func()

            while True:
                product = input("Enter the name of the stock you want to {} ".format(order_type))
                if product in market_data.columns:
                    print("input accepted")
                    break
                else:
                    print('product is not available, please select another product that is available')

            while True:
                try:
                    quantity = int(input("Enter the number of stocks you want to {} ".format(user_exp.order_type)))
                    break
                except:
                    print('Quantity is not correct, please enter a whole number')

            product_price = market_data.loc[date, product]

            # Execute order
            order = Order(user.user_id, product, quantity, order_type, product_price, date)
            order.trade()
            print(
                "You ordered {} ".format(order.quantity) + "stocks of {}".format(order.product) + ' on {}'.format(date)
                + ' for USD {}'.format(product_price) + ' per stock')

            # update portfolio
            portfolio_user.trade(order.trade_details)
            print(portfolio_user.get_positions())

            # check if user wants to make another trade
            answer = user_exp.trading_again()

            if answer == 'no':
                print("We hope you have had a great trading experience today. Your closing balance is as follows:")
                print(portfolio_user.calc_portfolio_value(market_data))
                print('We hope to see you again tomorrow. Have a good day!')
                break

    elif trade_indicator == 'no':
        print("We hope you have had a great trading experience, have a good day!")
        break

    counter += 1
