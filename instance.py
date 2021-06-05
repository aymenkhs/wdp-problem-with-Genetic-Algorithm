

class Bid:
    """
    a Class that represent a bid which is caracterized by:
            - the bider (an integer from 0 to n-1)
            - the price of the bundle (whole bid)
            - the items in the bundle
    """
    def __init__(self, bider, price, items):
        self.bider = bider
        self.price = price
        self.items = items

class InstanceWDP:
    """
    a Class that represent an instance of WDP which is caracterized by:
            - the number <n> of bids
            - the number <m> of items
            - a list of all the bids
    """
    def __init__(self, n, m, bids):
        self.n = n
        self.m = m
        self.bids = bids
