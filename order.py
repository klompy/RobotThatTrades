import itertools


# Class for managing orders, in a purely local version, just used for Order ID, in the future could expand to include most information the exchange sends regarding an order
class Order:    
    newid = itertools.count()

    def __init__(self):
        self.id = next(Order.newid)

