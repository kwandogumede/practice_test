
# Function to deposit money into an account
def deposit(account: dict, amount: float) -> None:
    to_deposit= 0
    for amount in account:
        new_balance=int(amount + to_deposit)
        return float(new_balance)

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:
    to_withdraw=0
    for amount in account:
        if to_withdraw < amount:
            new_balance=amount-to_withdraw
            return float(new_balance)

# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    for amount in from_account:
        for amount in to_account:
            return from_account[amount] + to_account[amount]

# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    newAccount=f"{owner}: balance:{initial_balance}"
    return newAccount

# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
        if owner in accounts:
            return accounts[owner]
        

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
