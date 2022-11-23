from hashlib import new


class cardHolder():
    def __init__(self, cardNum, pin, firstName, secondName, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstName = firstName
        self.secondName = secondName
        self.balance = balance

    ## Getters
    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_firstName(self):
        return self.firstName
    def get_secondName(self):
        return self.secondName
    def get_balance(self):
        return self.balance

    ## Setters
    def set_cardNum(self, newVal):
        self.cardNum = newVal
    def set_pin(self, newVal):
        self.pin = newVal
    def set_firstName(self, newVal):
        self.firstName = newVal
    def set_secondName(self, newVal):
        self.secondName = newVal
    def set_balance(self, newVal):
        self.balance = newVal

    def print_out(self):
        print("Card #: ", self.cardNum)
        print("Pin:  ", self.pin)
        print("First name: ", self.firstName)
        print("Last name: ", self.secondName)
        print("Balance: ", self.balance)