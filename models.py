import os
import json
import DataStructures
import session

class User:
    def __init__(self, name, username, password, income=0, expenses=0):
        self.name = name
        self.username = username
        self.password = password
        self.income = income
        self.expenses = expenses

class Tranasction:
    def __init__(self, ID, by, amount, date, category, description):
        self.ID = ID
        self.by = by
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

class Response: # 200 for success, 401 for bad request, 402 for user already exists, 500 for server error
    def __init__(self, success, message, code, load=None):
        self.success = success
        self.message = message
        self.code = code
        self.load = load
        
class Session:
    def __init__(self, user):
        self.user = user
        self.pages = DataStructures.Stack()
        self.transactions_list = []
        

Database_path = './Database'
users_path = os.path.join(Database_path, 'users.json')
session_path = os.path.join(Database_path, 'session.json')
transactions_path = os.path.join(Database_path, 'transactions.json')

def check_credentials(username, password):
    try:
        with open(users_path, 'r') as users_file:
            users = json.load(users_file)
        
        if username in users:
            user_data = users[username]

            if user_data['password'] == password:
                return Response(True, "Login successful", 200, User(user_data['name'], user_data['username'], password="*********", income=user_data['income'], expenses=user_data['expenses']))
            else:
                return Response(False, "Invalid Password", 401)
            
    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)


def check_exists(username):
    
    try:
        with open(users_path, 'r') as users_file:
            users = json.load(users_file)

        if username in users:
            return Response(True, "User exists", 200)
        else:
            return Response(False, "User does not exist", 401)

    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)
    

def push_user(new_user):

    try:

        if not os.path.exists(Database_path):
            os.mkdir(Database_path)

        if os.path.exists(users_path):
            with open(users_path, 'r') as users_file:
                users = json.load(users_file)
        else:
            users = {}

        users[new_user.username] = {
            'name': new_user.name,
            'username': new_user.username,
            'password': new_user.password,
            'income': new_user.income,
            'expenses': new_user.expenses
        }

        with open(users_path, 'w') as users_file:
            json.dump(users, users_file, indent=4)

        if os.path.exists(transactions_path):
            with open(transactions_path, 'r') as transactions_file:
                transaction = json.load(transactions_file)
        else:
            transaction = {}

        transaction[new_user.username] = []

        with open(transactions_path, 'w') as transactions_file:
            json.dump(transaction, transactions_file, indent=4)

        session.new_session(new_user)

        return Response(True, "User added successfully", 200)

    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)
    
    except Exception as e:
        return Response(False, f"An error occurred: {str(e)}", 500)


def get_incomes():
        
    try:
        with open(session_path, 'r') as sessions_file:
            data = json.load(sessions_file)

        return [ transaction for transaction in data["transactions_list"] if transaction["category"] == "income" ]


    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)
    
    except Exception as e:
        return Response(False, f"An error occurred: {str(e)}", 500)
    

def get_expenses():
        
    try:
        with open(session_path, 'r') as sessions_file:
            data = json.load(sessions_file)

        return [ transaction for transaction in data["transactions_list"] if transaction["category"] == "expenses" ]

    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)
    
    except Exception as e:
        return Response(False, f"An error occurred: {str(e)}", 500)

def sort_by_amount(username):
    try:
        PQ = DataStructures.MaxHeap(20)

        with open(transactions_path, 'r') as transactions_file:
            data = json.load(transactions_file)

        for transaction in data.get(username, []):
            PQ.insert(transaction)

        res = []
        
        while not PQ.is_empty():  
            res.append(PQ.remove())

        return res
        
    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)
    
    except Exception as e:
        return Response(False, f"An error occurred: {str(e)}", 500)

    
def get_transactions(username):
        
    try:
        with open(transactions_path, 'r') as transactions_file:
            transactions = json.load(transactions_file)

        return transactions[username]

    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)
    
    except Exception as e:
        return Response(False, f"An error occurred: {str(e)}", 500)

def add_transaction(id, by, amount, date, category, description):
        
    try:
        with open(transactions_path, 'r') as transactions_file:
            transactions = json.load(transactions_file)

        transactions[by].append({
            'ID': id,
            'by': by,
            'amount': amount,
            'date': date,
            'category': category,
            'description': description
        })

        with open(transactions_path, 'w') as transactions_file:
            json.dump(transactions, transactions_file, indent=4)

        with open(users_path, 'r') as users_file:
            users = json.load(users_file)

        if category == "income":
            users[by]['income'] += users[by].get('income', 0) + float(amount)
        else:
            users[by]['expenses'] += users[by].get('expenses', 0) + float(amount)

        with open(users_path, 'w') as users_file:
            json.dump(users, users_file, indent=4)
        
        return Response(True, "Transaction added successfully", 200)

    except FileNotFoundError:
        return Response(False, "Error connecting to DB", 500)
    
    except json.decoder.JSONDecodeError:
        return Response(False, "Error connecting to DB", 500)
    
    except Exception as e:
        return Response(False, f"An error occurred: {str(e)}", 500)