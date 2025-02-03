# OOP 
# Create a base class Account for a banking system with attributes like account_holder and balance 
# and methods like deposit() and withdraw(). Extend it into classes like SavingsAccount and CurrentAccount, 
# adding specific behavior (e.g., interest rate for SavingsAccount and overdraft limit for CurrentAccount).

class Account:
    def __init__(self, account_holder):# Initialize the Account with an account holder and balance
        self.__account_holder = account_holder #account holder
        self.__balance = 0.0 #balance 

    def get_account_holder(self): # Get the account holder's name
        return self.__account_holder #return account holder name
    def set_account_holder(self): # Set the account holder's name
        return self.__account_holder #return account holder name
    
    def get_balance(self): # Get the account balance
        return self.__balance #return account balance
    def set_balance(self, balance): # Set the account balance
        self.__balance = balance #set account balance

    def deposit(self, deposit_amount): # Deposit money into the account
        deposit_amount = float(input("Enter amount to deposit: ")) # Prompt user to enter amount to deposit
        if deposit_amount >= 0: # Check if the deposit amount is positive
          self.set_balance(self.get_balance() + deposit_amount) # Add the deposit amount to the balance
          print(f"Deposit of {deposit_amount} successful. New balance is {self.get_balance()}") # Print the new balance
        else:
           print("Invalid amount") # Print an error message if the deposit amount is negative

    def withdraw(self, withdraw_amount): # Withdraw money from the account
        withdraw_amount = float(input("Enter amount to withdraw: ")) # Prompt user to enter amount to withdraw
        if self.get_balance() >= withdraw_amount: # Check if there are sufficient funds in the account
            self.set_balance(self.get_balance() - withdraw_amount) # Subtract the withdrawal amount from the balance
            print(f"Withdrawal of {withdraw_amount} successful. New balance is {self.get_balance()}") # Print the new balance
        else:
            print("Insufficient funds") # Print an error message if there are insufficient funds

class SavingsAccount(Account):
    def __init__(self, account_holder, interest_rate=0.05):# Initialize the SavingsAccount with an interest rate
        super().__init__(account_holder)# Call the constructor of the parent class
        self.interest_rate = interest_rate # Set the interest rate for the SavingsAccount

    def add_interest(self): # Add interest to the account balance based on the interest rate
        interest = self.get_balance() * self.interest_rate # Calculate the interest amount
        self.set_balance(self.get_balance() + interest) # Add the interest to the balance
        print(f"Added interest of {interest}. New balance is {self.get_balance()}")# Print the new balance

class CurrentAccount(Account):
    def __init__(self, account_holder, overdraft_limit=1000.0):# Initialize the CurrentAccount with an overdraft limit
        super().__init__(account_holder)# Call the constructor of the parent class
        self.overdraft_limit = overdraft_limit # Set the overdraft limit for the CurrentAccount

    def withdraw(self, withdraw_amount):# Override the withdraw method to allow for overdraft
        if self.get_balance() + self.overdraft_limit >= withdraw_amount:
            self.set_balance(self.get_balance() - withdraw_amount)
            print(f"Withdrawal of {withdraw_amount} successful. New balance is {self.get_balance()}")
        else:
            print("Exceeded overdraft limit")

            
            # Create instances of the Account, SavingsAccount, and CurrentAccount classes
account = Account("John Doe") # Create an account for John Doe
savings_account = SavingsAccount("Jane Smith") # Create a savings account for Jane Smith
current_account = CurrentAccount("Alice Johnson") # Create a current account for Alice Johnson

# Perform operations on the accounts
account.deposit(500) # Deposit 500 into the current account
account.withdraw(200) # Withdraw 200 from the current account

