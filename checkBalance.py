## Check balance of cardholder
class CheckBalance:
    def __init__(self, cardHolder):
        self.cardHolder = cardHolder

    def check_balance(self):
        print("Your balance is: ", self.cardHolder.get_balance())