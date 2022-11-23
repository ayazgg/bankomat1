## Withdraw function
class Withdraw:
    def __init__(self, cardHolder, currency):
        self.cardHolder = cardHolder
        self.currency = currency

    def withdraw(self):
        try:
            withdraw = float(input("How much $$ would you like to withdraw"))
            if (self.cardHolder.get_balance() < withdraw):
                print("Not enough money")
            else:
                self.cardHolder.set_balance(self.cardHolder.get_balance() - withdraw)
                print("Operation finished successfully! You withdrew ", withdraw, self.currency)
        except:
            print("Invalid input")