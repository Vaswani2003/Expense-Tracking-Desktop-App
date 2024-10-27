import models
import random
import string
from datetime import datetime


def new_user_registration(name, username, password, confirm_password):

    if password != confirm_password:
        return models.Response(False, "Passwords do not match", 401)

    error = check_error_in_username(username)

    if error:
        return models.Response(False, "Invalid Username", 501)
    
    user_exists = models.check_exists(username)

    if user_exists.code == 200:
        return models.Response(False, "User Already Exists", 402)
    
    new_user = models.User(name, username, password)
    response = models.push_user(new_user)

    if response.success == False:
        models.Response(False, f"{response.message}", 500)

    return models.Response(True, "User Registered Successfully", 200, new_user)


def check_error_in_username(username):
    if len(username) < 3 or len(username) > 20:
        return True
    else:
        return False    

def login(username, password):

    user_exists = models.check_exists(username)

    if user_exists.success == False:
        return models.Response(False, "User does not exist", 401)

    response = models.check_credentials(username, password)

    if response.success:
        return models.Response(True, "Login successful", 200, response.load)

    elif response.code == 401:
        return models.Response(False, "Invalid Password", 402)


def get_transactions(username):
    return models.get_transactions(username)


def generate_random_id(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_transaction(username, transaction_type, amount, description):
    id = generate_random_id()
    date = get_current_datetime()

    response = models.add_transaction(id=id, by=username, amount=amount,date=date,category=transaction_type, description=description)
    return response

def sort_transactions_by_amount(username):
    return models.sort_by_amount(username)

# def get_transactions(username, filter_name):

#     if filter_name == "All Transactions":
#         return session.current_session().transactions_list
    
#     elif filter_name == "Income Only":
#         return models.get_incomes(session.current_user().username)
    
#     elif filter_name == "Expenses Only":
#         return models.get_expenses(session.current_user().username)
    
#     elif filter_name == "Sort by amount":
#         return models.sort_by_amount(session.current_user().username)
