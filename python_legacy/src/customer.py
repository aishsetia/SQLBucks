from database import Database
from models import CustomerBalance, Transaction as TransactionModel
from sqlalchemy.orm import Session
from datetime import datetime
from models import Customer as CustomerModel
import uuid

class Customer:
    def __init__(self, db: Database, cust_id: int):
        self.db: Session = db.session
        self.cust_id = cust_id
        db_customer = self.db.query(CustomerModel).filter(CustomerModel.cust_id == cust_id).first()
        if db_customer:
            self.name = db_customer.name
            self.address = db_customer.address
            self.dob = db_customer.dob
            self.gender = db_customer.gender
            self.phone = db_customer.phone
            self.email_id = db_customer.email_id
            self.occupation = db_customer.occupation

    @classmethod
    def new_customer(cls, db: Database, cust_id: int, name: str, address: str, dob: str, gender: str, phone: str, email_id: str, occupation: str):
        customer_obj = cls(db, cust_id)
        customer_obj.name = name
        customer_obj.address = address
        customer_obj.dob = dob
        customer_obj.gender = gender
        customer_obj.phone = phone
        customer_obj.email_id = email_id
        customer_obj.occupation = occupation
        db_customer = CustomerModel(cust_id=cust_id, name=name, address=address, dob=dob, gender=gender, phone=phone, email_id=email_id, occupation=occupation)
        customer_obj.db.add(db_customer)
        customer_obj.db.commit()
        return customer_obj

    def deposit_money(self, amount: float):
        customer_balance = self.db.query(CustomerBalance).filter(CustomerBalance.cust_id == self.cust_id).first()
        customer_balance.balance += amount
        customer_balance.last_transaction_time = datetime.now()
        
        Transaction.record_transaction(self.db, None, self.cust_id, amount)
        self.db.commit()
        self.display_balance()

    def withdraw_money(self, amount: float):
        customer_balance = self.db.query(CustomerBalance).filter(CustomerBalance.cust_id == self.cust_id).first()
        customer_balance.balance -= amount
        customer_balance.last_transaction_time = datetime.now()
        
        Transaction.record_transaction(self.db, self.cust_id, None, amount)
        self.db.commit()
        self.display_balance()

    def transfer_money(self, target_cust_id: int, amount: float):
        source_balance = self.db.query(CustomerBalance).filter(CustomerBalance.cust_id == self.cust_id).first()
        target_balance = self.db.query(CustomerBalance).filter(CustomerBalance.cust_id == target_cust_id).first()
        
        source_balance.balance -= amount
        source_balance.last_transaction_time = datetime.now()
        
        target_balance.balance += amount
        target_balance.last_transaction_time = datetime.now()
        
        Transaction.record_transaction(self.db, self.cust_id, target_cust_id, amount)
        self.db.commit()
        self.display_balance()

    def display_balance(self):
        customer_balance = self.db.query(CustomerBalance).filter(CustomerBalance.cust_id == self.cust_id).first()
        print(f"Updated Balance: {customer_balance.balance}")

class Transaction:
    @staticmethod
    def record_transaction(db: Database, dcust: int, ccust: int, amount: float):
        transac_id = int(uuid.uuid4()) & 0x7FFFFFFF
        transaction = TransactionModel(transac_id=transac_id, dcust=dcust, ccust=ccust, amount=amount, timestamp=datetime.now())
        db.add(transaction)
        db.commit()