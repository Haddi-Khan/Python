class ATM:
    def __init__(self, pin, balance=1000):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin

    def check_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print("Your balance is:", self.balance)
        else:
            print("Wrong PIN!")

    def deposit(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Wrong PIN!")

    def withdraw(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN!")
atm = ATM("1234", 5000)
atm.check_balance("1234")     
atm.deposit("1234", 1000)     
atm.withdraw("1234", 2000)    
atm.withdraw("0000", 1000)    