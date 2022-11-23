from hashlib import new


class currency():
    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    ## Getters
    def get_currency(self):
        return self.currency
    def get_rate(self):
        return self.rate

    def set_rate(self, newVal):
        self.rate = newVal

    def convert_to(self, amount):
        return amount * self.rate

    def convert_from(self, amount):
        return amount / self.rate

    def print_out(self):
        print("Card #: ", self.cardNum)
        print("Pin:  ", self.pin)
        print("First name: ", self.firstName)
        print("Last name: ", self.secondName)
        print("Balance: ", self.balance)