from database import Database
from models import Customer, Transaction, CustomerBalance
from sqlalchemy.orm import Session
from tabulate import tabulate

class Admin:
    def __init__(self, db: Database):
        self.db: Session = db.session

    def find_customer(self, cust_id: int):
        customer = self.db.query(Customer).filter(Customer.cust_id == cust_id).first()
        if customer:
            for key, value in customer.__dict__.items():
                if not key.startswith('_'):
                    print(f"{key}: {value}")
        else:
            print("Customer not found.")

    def view_ledger(self):
        balances = self.db.query(CustomerBalance).all()
        table = [{k: v for k, v in balance.__dict__.items() if not k.startswith('_')} for balance in balances]
        print(tabulate(table, headers="keys", tablefmt="pretty"))

    def view_transactions(self):
        transactions = self.db.query(Transaction).all()
        table = [{k: v for k, v in txn.__dict__.items() if not k.startswith('_')} for txn in transactions]
        print(tabulate(table, headers="keys", tablefmt="pretty"))

    def locate_transaction(self, transac_id: int):
        txn = self.db.query(Transaction).filter(Transaction.transac_id == transac_id).first()
        if txn:
            table = [{k: v for k, v in txn.__dict__.items() if not k.startswith('_')}]
            print(tabulate(table, headers="keys", tablefmt="pretty"))
        else:
            print("Transaction not found.") 