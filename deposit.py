# Deposit
class Deposit:
    def __init__(self, cardHolder, currency):
        self.cardHolder = cardHolder
        self.currency = currency

    def deposit(self):
        try:
            deposit = float(input("How much money would you like to deposit?"))
            self.cardHolder.set_balance(self.cardHolder.get_balance() + deposit)
            print("Operation finished successfully! You deposited ", deposit, self.currency)
        except:
            print("Invalid input")