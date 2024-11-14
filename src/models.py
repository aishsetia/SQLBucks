from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'credentials'

    userid = Column(String(50), primary_key=True, index=True)
    pwd_hash = Column(String(255), nullable=False)
    cust_id = Column(Integer, ForeignKey('customerdetails.cust_id'))
    admin = Column(Boolean, default=False)

    customer = relationship("Customer", back_populates="user")

class Customer(Base):
    __tablename__ = 'customerdetails'

    cust_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    address = Column(String(255))
    dob = Column(String(10))
    gender = Column(String(20))
    phone = Column(String(15))
    email_id = Column(String(100), unique=True)
    occupation = Column(String(100))

    balance = relationship("CustomerBalance", back_populates="customer")
    user = relationship("User", back_populates="customer")
    
    # Define separate relationships for sent and received transactions
    sent_transactions = relationship(
        "Transaction",
        foreign_keys="Transaction.dcust",
        back_populates="sender"
    )
    received_transactions = relationship(
        "Transaction",
        foreign_keys="Transaction.ccust",
        back_populates="receiver"
    )

class CustomerBalance(Base):
    __tablename__ = 'customerbalance'

    cust_id = Column(Integer, ForeignKey('customerdetails.cust_id'), primary_key=True)
    balance = Column(Float, default=0.0)
    last_transaction_time = Column(DateTime)

    customer = relationship("Customer", back_populates="balance")

class Transaction(Base):
    __tablename__ = 'transactions'

    transac_id = Column(Integer, primary_key=True, index=True)
    dcust = Column(Integer, ForeignKey('customerdetails.cust_id'), nullable=True)
    ccust = Column(Integer, ForeignKey('customerdetails.cust_id'), nullable=True)
    amount = Column(Float)
    timestamp = Column(DateTime)

    # Define relationships with explicit foreign keys
    sender = relationship(
        "Customer",
        foreign_keys=[dcust],
        back_populates="sent_transactions"
    )
    receiver = relationship(
        "Customer",
        foreign_keys=[ccust],
        back_populates="received_transactions"
    ) 