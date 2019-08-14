#Classes file
import numpy as np
import pandas as pd

#Define class User
class User:

    def __init__(self, surname: str, firstname: str) -> None:
        if surname == "":
            raise ValueError("Surname not defined, please enter your surname")
        else:
            self._surname = surname
        if firstname == "":
            raise ValueError("Name not defined, please enter your name")
        else:
            self._firstname = firstname

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def name(self) -> str:
        return self._firstname

    @property
    def fullname(self) -> str:
        return self._surname + " " + self._firstname

    @property
    def user_id(self) -> str:
        return self._surname + self._firstname


# Define class Order that creates an order
class Order:
    def __init__(self, user_id, product, quantity, order_type, product_price, order_date):
        self.user_id = user_id
        self.product = product
        self.quantity = quantity
        self.order_type = order_type
        self.product_price = product_price
        self.order_date = order_date
        self.trade_details = []

    def trade(self):
        order_action = input("Are you sure you want to place this order 'yes'/'no' ? ")
        if order_action == 'yes':
            if self.order_type == 'buy':
                trade = [self.user_id, self.product, self.quantity, self.order_type, self.product_price ,
                         self.order_date]
            elif self.order_type == 'sell':
                self.quantity = -1*self.quantity
                trade = [self.user_id, self.product, self.quantity, self.order_type, self.product_price,
                         self.order_date]
        elif order_action == 'no':
            trade = [np.isnan, np.isnan, np.isnan, np.isnan, np.isnan]
        self.trade_details = trade


class Portfolio:
    def __init__(self, user, position):
        self.user = user
        self.position = position

    def trade(self, trade):
        self.product = trade[1]
        self.quantity = trade[2]
        self.ordertype = trade[3]
        self.date = trade[5]

        if self.date in self.position.index:
            self.position.loc[self.date, self.product] += self.quantity
        else:
            self.position.loc[self.date] = pd.Series([0.0] * len(self.position.columns))
            self.position.loc[self.date] = 0
            self.position.loc[self.date] = self.position.iloc[self.position.index.get_loc(self.date) - 1, :]
            self.position.loc[self.date, self.product] += self.quantity

        return "Trade processed: {} shares of {}.".format(self.quantity, self.product)

    def get_positions(self):
        m1 = (self.position.loc[self.date, :] != 0)
        m2 = self.position.loc[self.date, m1]
        df1 = pd.DataFrame(m2)
        df1.columns = ['Quantity']
        return df1

    def calc_portfolio_value(self, market_data):
        portfolio_balance = pd.DataFrame(columns=['date', 'balance'])

        for date in self.position.index:
            balance = 0
            for stock in self.position.columns:
                balance_temp = market_data.loc[date, stock] * self.position.loc[date, stock]
                balance += balance_temp

            portfolio_balance = portfolio_balance.append(pd.DataFrame([[date, balance]], columns=portfolio_balance.columns))
            portfolio_balance.set_index('date', inplace = True)

        return portfolio_balance
