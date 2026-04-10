class bankaccount:
    def __init__(self,account_holder, balance=0):
        self.account_holder= account_holder
        self.balance=balance
        print(f"Account created for {self.account_holder} with initial balance: {self.balance}")
    def deposit(self,amount):
        if amount >= 500:
            self.balance = self.balance + amount
            print(f"The amount {amount} has been deposit to your account, your current balance is {self.balance} ")
        else:
            print("Amount can not be deposite")
    def withdraw (self,amount):
        if amount >= 500:
            if amount <= self.balance:
                self.balance = self.balance - amount
                print (f"Your aoumnt has been withdraw {amount} Thank you for using bank account, Your current balance is {self.balance}")
            else:
                print(f"Balance is low, your current balance is {self.balance}")
        else:
            print (f"Your amount cannot be withdraw amount {amount} should be greater and equal to the 500")
    def check_balance (self):
         print(f"Current Balance: {self.balance}")
account = bankaccount("Haddi",2000)
account.deposit(1000)
account.withdraw(2000)
