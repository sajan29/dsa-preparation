from datetime import datetime
class Response:
    OK = "OK"
    ERROR = "ERROR"

class LedgerType:
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

class Account:
    def __init__(self, account_id):
        self.account_id = account_id
        self.ledger_entries = []

entry_id = 1
class LedgerEntry:
    def __init__(self, type, amount):
        global entry_id
        self.entry_id = entry_id
        entry_id+=1
        self.timestamp = datetime.now().timestamp()
        self.type = type
        self.amount = amount

# Collection of Accounts
accounts = {}
# Balance Cache Look Up
balance_cache = {}

def get_account(account_id):
    return accounts.get(account_id)

def create_account(account_id):
    account = get_account(account_id)
    if account is not None:
        return Response.ERROR
    accounts[account_id] = Account(account_id)
    return Response.OK

def post_entries(type, account_id, amount):
    account = get_account(account_id)
    if account is None:
        return Response.ERROR
    if type not in [LedgerType.CREDIT, LedgerType.DEBIT]:
        return Response.ERROR
    if amount <= 0:
        return Response.ERROR
    balance = get_balance(account_id)
    if type == LedgerType.DEBIT and (balance-amount) < 0:
        return Response.ERROR
    account.ledger_entries.append(LedgerEntry(type, amount))
    return Response.OK

def get_balance(account_id):
    account = get_account(account_id)
    if account is None:
        return Response.ERROR
    balance = 0
    for ledger_entry in account.ledger_entries:
        if ledger_entry.type == LedgerType.CREDIT:
            balance += ledger_entry.amount
        elif ledger_entry.type == LedgerType.DEBIT:
            balance -= ledger_entry.amount
    return balance

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    line = line.split()
    command = line[0]
    account_id = line[1]
    if command == "CREATE_ACCOUNT":
        print(create_account(account_id))
    elif command in [LedgerType.CREDIT, LedgerType.DEBIT]:
        amount = int(line[2])
        print(post_entries(command, account_id, amount))
    elif command == "BALANCE":
        print(get_balance(account_id))




    