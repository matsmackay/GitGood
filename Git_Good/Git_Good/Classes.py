#Classes file
import numpy as np

#Define clas User
class User:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
        self.fullname = self.surname + " " + self.name
        self.user_id = self.surname + self.name


# Define class Order that creates an order
class Order:
    def __init__(self, user_id, product, quantity):
        self.user_id = user_id
        self.product = product
        self.quantity = quantity

    def trade(self):
        order_action = input("Are you sure you want to place this order 'yes'/'no' ? ")
        if order_action == 'yes':
            trade = [self.user_id, self.product, self.quantity]
            return trade
        elif order_action == 'no':
            trade = [np.isnan, np.isnan, np.isnan]
            return trade


class Portfolio:
    def __init__(self, user, position=position):
        self.user = user
        self.position = position

    def trade(self, product, quantity):
        self.position[product] += quantity

    def get_positions(self, position=position):
        position2 = [(key, value) for (key, value) in position.items() if value != 0]
        df1 = pd.DataFrame(position2)
        df1.columns = ['Product', 'Quantity']
        df1.set_index('Product', inplace=True)
        return df1
