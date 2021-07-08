

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

        self.concurent_bids = []


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

    def __getitem__(self, index):
        return self.bids[index]

    def build_concurent_items(self):
        for bid in self.bids:
            for potential_concurents in self.bids:
                if bid != potential_concurents:
                    for item in bid.items:
                        if item in potential_concurents.items:
                            bid.concurent_bids.append(potential_concurents)
                            break
