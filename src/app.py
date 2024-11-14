from database import Database
from models import User, CustomerBalance
from customer import Customer
from admin import Admin
import getpass
from sqlalchemy.orm import Session
import bcrypt
import uuid
def welcome_message():
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('*****  WELCOME TO BANK OF E  *****')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def register_user(db: Database):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    gender = input("Enter your gender (Male/Female/Trans/Non-Binary): ")
    phone = input("Enter your 10-digit mobile number: ")
    email = input("Enter your email-id: ")
    occupation = input("Enter your occupation: ")
    cust_id = int(uuid.uuid4()) & 0x7FFFFFFF

    new_customer = Customer.new_customer(
        db=db,
        cust_id=cust_id,
        name=name,
        address=address,
        dob=dob,
        gender=gender,
        phone=phone,
        email_id=email,
        occupation=occupation
    )
    user = User(
        userid=f"{new_customer.cust_id}.{name[0].upper()}",
        pwd_hash=bcrypt.hashpw(getpass.getpass("Set your password: ").encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
        cust_id=new_customer.cust_id,
        admin=False
    )
    db.session.add(user)

    customer_balance = CustomerBalance(cust_id=new_customer.cust_id, balance=0.00)
    db.session.add(customer_balance)

    db.session.commit()

    print(f"Account registered successfully. Your username is: {user.userid}")

def login_user(db: Database):
    userid = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    user = db.session.query(User).filter(User.userid == userid).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.pwd_hash.encode('utf-8')):
        print("LOGIN SUCCESSFUL")
        return user
    else:
        print("LOGIN FAILED: Invalid credentials.")
        return None

def customer_menu(db: Database, customer: Customer):
    while True:
        print('Press 1 for depositing money')
        print('Press 2 for withdrawing money')
        print('Press 3 for checking balance')
        print('Press 4 to transfer money to another account')
        print('Press 5 for logging out')
        choice = input("Option: ")
        if choice == '1':
            amount = float(input("Amount to deposit: "))
            customer.deposit_money(amount)
        elif choice == '2':
            amount = float(input("Amount to withdraw: "))
            customer.withdraw_money(amount)
        elif choice == '3':
            customer.display_balance()
        elif choice == '4':
            target_id = int(input("Enter target customer ID: "))
            amount = float(input("Amount to transfer: "))
            customer.transfer_money(target_id, amount)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def admin_menu(db: Database, admin: Admin):
    while True:
        print('Press 1 for finding customer')
        print('Press 2 for viewing ledger')
        print('Press 3 for viewing transaction table')
        print('Press 4 for locating a transaction')
        print('Press 5 to log out')
        choice = input("Option: ")
        if choice == '1':
            cust_id = int(input("Enter Customer ID: "))
            admin.find_customer(cust_id)
        elif choice == '2':
            admin.view_ledger()
        elif choice == '3':
            admin.view_transactions()
        elif choice == '4':
            transac_id = int(input("Enter Transaction ID: "))
            admin.locate_transaction(transac_id)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def main():
    db = Database()
    while True:
        welcome_message()
        print('Press 1 for Online Banking')
        print('Press 2 for Registering a new bank account')
        print('Press 3 for Deleting your account')
        print('Press 4 for Admin Panel')
        print('Press 5 for Exit')
        choice = input("Option: ")
        if choice == '1':
            user = login_user(db)
            if user:
                if user.admin:
                    admin = Admin(db)
                    admin_menu(db, admin)
                else:
                    customer = Customer(db, user.cust_id)
                    customer_menu(db, customer)
        elif choice == '2':
            register_user(db)
        elif choice == '3':
            user = login_user(db)
            if user and not user.admin:
                # Implement account deletion
                confirm = input("Are you sure you want to delete your account? (yes/no): ")
                if confirm.lower() == 'yes':
                    db.session.delete(user)
                    db.session.commit()
                    print("Account deleted successfully.")
        elif choice == '4':
            user = login_user(db)
            if user and user.admin:
                admin = Admin(db)
                admin_menu(db, admin)
            else:
                print("Access denied: Admins only.")
        elif choice == '5':
            print("Exiting the application.")
            db.close()
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main() 