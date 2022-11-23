# Pay for phone
class PayForPhone:
    def __init__(self, cardHolder):
        self.cardHolder = cardHolder

    def pay_for_phone(self):
        try:
            phone = int(input("Type your phone number: "))
            pay_for_phone = float(input("How much money would you like to pay for your phone?"))
            if (self.cardHolder.get_balance() < pay_for_phone):
                print("Not enough money")
            else:
                self.cardHolder.set_balance(self.cardHolder.get_balance() - pay_for_phone)
                print("Operation finished successfully! You paid ", pay_for_phone, "$ for phone number: ", phone)
        except:
            print("Invalid input")