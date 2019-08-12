
position = {'A': 0, 'B': 0, 'C': 0}


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

