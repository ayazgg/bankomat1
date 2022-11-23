from os import curdir
from tkinter import W
from unittest import expectedFailure
from cardHolder import cardHolder
from checkBalance import CheckBalance
from deposit import Deposit
from payForPhone import PayForPhone
from withdraw import Withdraw
from currencyChange import currency

def print_menu():
    print("Please choose from one of the following options...")
    print("Your current currecny is: ", current_currency.get_currency())
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Pay for mobile phone")
    print("5. Exit")

def print_currency_menu():
    print("Please choose from one of the following options...")
    print("1. USD")
    print("2. BYN")

if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", "")
    current_currency = currency("USD", 1)

    # List of currency
    list_of_currency = []
    list_of_currency.append(currency("USD", 1))
    list_of_currency.append(currency("BYN", 2.55))

    ### Create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("4278320021135321", 1234, "Ikromjon", "Akhmadjonov", 0))
    list_of_cardHolders.append(cardHolder("8600490487880809", 2003, "Ikromjon", "Akhmadjonov", 0))

    ### Promt user for devit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if (len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card num not recognised. Please try again")    
        except:
            print("Card num not recognised. Please try again")

## Promt for PIN and no more than 3 attempts
    pin = ""
    attempts = 0
    while True:
        try:
            pin = int(input("Please insert your PIN: "))
            if (pin == current_user.pin):
                break
            else:
                attempts += 1
                print("Incorrect PIN. Please try again")
                if (attempts == 3):
                    print("Too many attempts. Your card has been blocked")
                    exit()
        except:
            exit()


## 
print("Welcome ", current_user.get_firstName(), " :)")
option = 0
currency_option = 0
while (option != 3):
    print_currency_menu()
    currency_option = int(input("Please choose your currency: "))
    if (currency_option == 1):
        current_currency = list_of_currency[0]
        while option != 5:
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid input. Please try again.")
            if (option == 1):
                Deposit(current_user, current_currency.get_currency()).deposit()
            elif (option == 2):
                Withdraw(current_user, current_currency.get_currency()).withdraw()
            elif (option == 3):
                CheckBalance(current_user, current_currency.get_currency()).check_balance()
            elif (option == 4):
                PayForPhone(current_user).pay_for_phone()
            elif (option == 5):
                break
            else:
                open = 0
    elif (currency_option == 2):
        current_currency = list_of_currency[1]
        while option != 5:
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid input. Please try again.")
            if (option == 1):
                Deposit(current_user, current_currency.get_currency()).deposit()
            elif (option == 2):
                Withdraw(current_user, current_currency.get_currency()).withdraw()
            elif (option == 3):
                CheckBalance(current_user, current_currency.get_currency()).check_balance()
            elif (option == 4):
                PayForPhone(current_user).pay_for_phone()
            elif (option == 5):
                break
            else:
                open = 0

print("Thank you. Have a nice day")