import bcrypt
import uuid
from database import Database
from models import User, Customer, CustomerBalance

def create_admin(db: Database):
    # Hash the admin password
    password = 'adminpassword'
    pwd_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    cust_id = int(uuid.uuid4()) & 0x7FFFFFFF

    # Create Admin Customer
    admin_customer = Customer(
        cust_id=cust_id,
        name='Aishwarya Setia',
        address='123 Admin Street',
        dob='1970-01-01',
        gender='Other',
        phone='0000000000',
        email_id='admin@example.com',
        occupation='Administrator'
    )

    # Create Admin User
    admin_user = User(
        userid=f"{cust_id}.A",
        pwd_hash=pwd_hash,
        cust_id=cust_id,
        admin=True
    )

    # Create Admin Customer Balance
    admin_balance = CustomerBalance(
        cust_id=cust_id,
        balance=100000.00,
        last_transaction_time=None
    )

    # Add to session and commit
    db.session.add(admin_customer)
    db.session.add(admin_user)
    db.session.add(admin_balance)
    db.session.commit()
    print(f"Admin account created with userid: {admin_user.userid} and password: {password}")

def create_dummy_users(db: Database):
    # Hash the user password
    password = f"mehularora"
    pwd_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    cust_id = int(uuid.uuid4()) & 0x7FFFFFFF

    # Create Dummy Customer
    customer1 = Customer(
        cust_id=cust_id,
        name='Mehul Arora',
        address=f'Dummy Ave',
        dob='2003-10-08',
        gender='Male',
        phone=f'1234567890',
        email_id=f'dummy1@example.com',
        occupation='Tester'
    )

    # Create Dummy User
    user1 = User(
        userid=f"{cust_id}.U",
        pwd_hash=pwd_hash,
        cust_id=cust_id,
        admin=False
    )

    # Create Dummy Customer Balance
    balance1 = CustomerBalance(
        cust_id=cust_id,
        balance=1000.00,
        last_transaction_time=None
    )
    
        # Hash the user password
    password = f"mehularora"
    pwd_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    cust_id = int(uuid.uuid4()) & 0x7FFFFFFF

    # Create Dummy Customer
    customer2 = Customer(
        cust_id=cust_id,
        name='Vania Setia',
        address=f'Dummy Ave',
        dob='2004-04-23',
        gender='Female',
        phone=f'1234567890',
        email_id=f'dummy2@example.com',
        occupation='Tester'
    )

    # Create Dummy User
    user2 = User(
        userid=f"{cust_id}.U",
        pwd_hash=pwd_hash,
        cust_id=cust_id,
        admin=False
    )

    # Create Dummy Customer Balance
    balance2 = CustomerBalance(
        cust_id=cust_id,
        balance=1000.00,
        last_transaction_time=None
    )

    # Add to session
    db.session.add(customer1)
    db.session.add(user1)
    db.session.add(balance1)
    db.session.add(customer2)
    db.session.add(user2)
    db.session.add(balance2)
    print(f"Created dummy user {user1.userid} with password: {password}")
    print(f"Created dummy user {user2.userid} with password: {password}")

    # Commit all dummy users
    db.session.commit()
    print("Dummy accounts created.")

def main():
    db = Database()
    create_admin(db)
    create_dummy_users(db)
    db.close()

if __name__ == "__main__":
    main() 