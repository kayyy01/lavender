PIN = "5034"
balance = 1000.00
history = {}

def check_balance():
    print(f"Your current balance is {balance}")

def deposit_money(balance):
    user_deposit = float(input("how much do you want to deposit"))
    if user_deposit > 0: 
        balance += user_deposit
        print(f"{user_deposit} has been deposited into your account. \n Your current balance is {balance}")
        history["deposit"] = user_deposit
        return balance
    
    if user_deposit < 0:
        print("Invalid amount")


def withdraw_money(balance):
    user_withdraw =  float(input("how much do you want to withdraw?"))
    if user_withdraw <= balance:
        balance -= user_withdraw
        print(f"{user_withdraw} has been deposited into your account. \n Your current balance is {balance}")
        history['withdrawals'] = user_withdraw
        return balance
    
    
    if user_input < 0:
        print("Invalid amount")
    
    if user_input > balance:
        print("Insufficient balance to complete this transaction")



def view_history():
    print(history)

#welcome page for user
#user enters 4 digit pin
input_pin = input("Welcome to BANK ATM \n enter your 4 digit pin to continue ")

#incase pin is wrong
if input_pin != PIN:
    print("Invalid user pin \n please try again")
    input_pin = input("enter your 4 digit code")


#if pin is right
if input_pin == PIN:
    while True:
        print(''''
            1. check balance
            2. deposit money
            3. withdraw money
            4. View transaction history
            5. Exit
            ''')
        user_input = input("Choose an option ")

        if user_input == "1":
            check_balance()    

        if user_input == "2":
            deposit_money(balance)

        if user_input == "3":
            withdraw_money(balance)
        
        if user_input == "4":
            view_history()

        if user_input == "5":
            print("See you next time. Adios!")
            break

    






