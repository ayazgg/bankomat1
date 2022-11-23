## Check balance of cardholder
class CheckBalance:
    def __init__(self, cardHolder, currency):
        self.cardHolder = cardHolder
        self.currency = currency

    def check_balance(self):
        print("Your balance is: ", self.cardHolder.get_balance(), self.currency)