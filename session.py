import os
import json
import models

Database_path = './Database'
users_path = os.path.join(Database_path, 'users.json')
session_path = os.path.join(Database_path, 'session.json')
transactions_path = os.path.join(Database_path, 'transactions.json')


# class Session:
#     def __init__(self, user):
#         self.user = user
#         self.pages = DataStructures.Stack()
#         self.transactions_list = []

def create():
    return models.Session(models.User("", "", ""))

def create_session(user):
    try:
        session = models.Session(user)

        with open(session_path, 'w') as session_file:
            json.dump(session.__dict__, session_file)

        return models.Response(True, "Session created", 200)
    
    except Exception as e:
        return models.Response(False, "Error creating session", 500)
    
def update_session_transactions(transactions_list):
    try:
        with open(session_path, 'r') as session_file:
            session = json.load(session_file)
        
        session['transactions_list'] = transactions_list

        with open(session_path, 'w') as session_file:
            json.dump(session, session_file)

        return models.Response(True, "Session updated", 200)
    
    except Exception as e:
        return models.Response(False, "Error updating session", 500)
    
def current_session():
    try:
        with open(session_path, 'r') as session_file:
            session = json.load(session_file)
        
        return models.Response(True, "User data is in the load", 200, load=session)
    
    except Exception as e:
        return models.Response(False, "Error getting session", 500)
    
def load_session():
    try:
        with open(session_path, 'r') as session_file:
            session = json.load(session_file)
        
        return models.Response(True, "User data is in the load", 200, load=session)
    
    except Exception as e:
        return models.Response(False, "Error loading session", 500)
    
