from collections import defaultdict
from datetime import datetime
class Account:
    # Account Class
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0
        self.transactions = []

next_transaction_id = 1

class Transaction:
    def __init__(self, transaction_type, amount):
        global next_transaction_id
        self.transaction_id = next_transaction_id
        next_transaction_id += 1
        self.transaction_type = transaction_type
        self.amount = amount

accounts = {}

def create_account(account_id):
    if get_account(account_id) is not None:
        return "ERROR"
    accounts[account_id] = Account(account_id) # Initialize balance to zero
    return "OK"

def get_account(account_id):
    return accounts.get(account_id)
    
def deposit(account_id, amount):
    account = get_account(account_id)
    if account is None:
        return "ERROR"
    if amount <=0:
        return "ERROR"
    account.balance = account.balance + amount
    account.transactions.append(Transaction("DEPOSIT", amount))
    return "OK"

def withdraw(account_id, amount):
    account = get_account(account_id)
    if account is None:
        return "ERROR"
    if amount <=0 or account.balance < amount:
        return "ERROR"
    account.balance = account.balance - amount
    account.transactions.append(Transaction("WITHDRAW", amount))
    return "OK"

def get_balance(account_id):
    account = get_account(account_id)
    if account is None:
        return "ERROR"
    return account.balance

def transfer_money(source_id, destination_id, amount):

    source = get_account(source_id)
    destination = get_account(destination_id)

    if source is None or destination is None:
        return "ERROR"

    if source_id == destination_id:
        return "ERROR"

    if amount <= 0:
        return "ERROR"

    if source.balance < amount:
        return "ERROR"

    source.balance -= amount
    destination.balance += amount

    source.transactions.append(
        Transaction("TRANSFER_OUT", amount)
    )

    destination.transactions.append(
        Transaction("TRANSFER_IN", amount)
    )

    return "OK"

def get_transactions(account_id):
    account = get_account(account_id)
    if account is not None:
        for t in account.transactions:
            print(f"{t.transaction_id} {t.transaction_type} {t.amount}")
        return "OK"
    else:
        return "ERROR"


while True:
    try:
        line = input().strip()
    except EOFError:
        break 
    if not line:
        continue
    input_string = line.split()
    command = input_string[0]
    if command == "CREATE_ACCOUNT":
        account_id = input_string[1] 
        print(create_account(account_id))
    elif command == "DEPOSIT":
        account_id = input_string[1]
        amount = int(input_string[2])
        print(deposit(account_id, amount))
    elif command == "WITHDRAW":
        account_id = input_string[1]
        amount = int(input_string[2])
        print(withdraw(account_id, amount))
    elif command == "BALANCE":
        account_id = input_string[1]
        print(get_balance(account_id))
    elif command == "TRANSFER":
        source_account_id = input_string[1]
        destination_account_id = input_string[2]
        amount = int(input_string[3])
        print(transfer_money(source_account_id, destination_account_id, amount))
