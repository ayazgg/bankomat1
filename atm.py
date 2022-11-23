from os import curdir
from tkinter import W
from unittest import expectedFailure
from cardHolder import cardHolder
from checkBalance import CheckBalance
from currencyChange import currency
from deposit import Deposit
from payForPhone import PayForPhone
from withdraw import Withdraw
from payBills import PayForBills

def print_menu():
    print("Please choose from one of the following options...")
    print("Your current currecny is: ", current_currency.get_currency())
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Pay for mobile phone")
    print("5. Exit")

if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", "")

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


## Print options
print("Welcome ", current_user.get_firstName(), " :)")
option = 0
while option != 6:
    print_menu()
    try:
        option = int(input())
    except:
        print("Invalid input. Please try again.")
    if (option == 1):
        Deposit(current_user).deposit()
    elif (option == 2):
        Withdraw(current_user).withdraw()
    elif (option == 3):
        CheckBalance(current_user).check_balance()
    elif (option == 4):
        PayForPhone(current_user).pay_for_phone()
    elif (option == 5):
        PayForBills(current_user).pay_for_bills()
    elif (option == 6):
        break
    else:
        open = 0
    
print("Thank you. Have a nice day")