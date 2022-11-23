# Pay for bills
class PayForBills:
    def __init__(self, cardHolder):
        self.cardHolder = cardHolder

    def pay_for_bills(self):
        try:
            bill = int(input("Type your bill number: "))
            pay_for_bills = float(input("How much money would you like to pay for your bill?"))
            if (self.cardHolder.get_balance() < pay_for_bills):
                print("Not enough money")
            else:
                self.cardHolder.set_balance(self.cardHolder.get_balance() - pay_for_bills)
                print("Operation finished successfully! You paid ", pay_for_bills, "$ for bill number: ", bill)
        except:
            print("Invalid input")