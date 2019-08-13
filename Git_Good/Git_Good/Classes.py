#Classes file
import numpy as np
import pandas as pd

#Define class User
class User:
    def __init__(self, surname, name):
        self._surname = surname
        self._name = name
        self._fullname = self.surname + " " + self.name
        self._user_id = self.surname + self.name


# Define class Order that creates an order
class Order:
    def __init__(self, user_id, product, quantity, order_type, product_price, order_date):
        self.user_id = user_id
        self.product = product
        self.quantity = quantity
        self.order_type = order_type
        self.product_price = product_price
        self.order_date = order_date

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
            return trade
        elif order_action == 'no':
            trade = [np.isnan, np.isnan, np.isnan, np.isnan, np.isnan]
            return trade

class Portfolio:
    def __init__(self, user, position):
        self.user = user
        self.position = position

    def trade(self, product, quantity):
        self.position[product] += quantity

    def get_positions(self):
        position2 = [(key, value) for (key, value) in self.position.items() if value != 0]
        df1 = pd.DataFrame(position2)
        df1.columns = ['Product', 'Quantity']
        df1.set_index('Product', inplace=True)
        return df1
