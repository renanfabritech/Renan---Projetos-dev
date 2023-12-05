
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a class for the financial system
class FinancialSystem:
    def __init__(self, company_name):
        self.company_name = company_name
        self.accounts = {}
    
    def add_account(self, account_name, initial_balance):
        self.accounts[account_name] = initial_balance
    
    def deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name] += amount
        else:
            print("Account not found.")
    
    def withdraw(self, account_name, amount):
        if account_name in self.accounts:
            if self.accounts[account_name] >= amount:
                self.accounts[account_name] -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")
    
    def get_balance(self, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name]
        else:
            print("Account not found.")
    
    def plot_accounts(self):
        plt.bar(self.accounts.keys(), self.accounts.values())
        plt.xlabel("Accounts")
        plt.ylabel("Balance")
        plt.title("Account Balances")
        plt.show()

# Create an instance of the FinancialSystem class
financial_system = FinancialSystem("ABC Company")

# Add accounts to the financial system
financial_system.add_account("Checking Account", 1000)
financial_system.add_account("Savings Account", 5000)

# Deposit and withdraw from accounts
financial_system.deposit("Checking Account", 500)
financial_system.withdraw("Savings Account", 1000)

# Get account balances
checking_balance = financial_system.get_balance("Checking Account")
savings_balance = financial_system.get_balance("Savings Account")

# Print the account balances
print("Checking Account Balance:", checking_balance)
print("Savings Account Balance:", savings_balance)

# Plot the account balances
financial_system.plot_accounts()