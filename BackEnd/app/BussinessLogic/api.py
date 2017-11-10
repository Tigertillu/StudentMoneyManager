'''
BUSSINESS LOGIC, that handles complex functionalities

Author: Manoj Vignesh K M
version : 1.0.0
Date : 8 November 2017
'''
import app.DBdriver.driver as driver

'''
function to authenticate a user by comparing 
the password of the username against the set password
'''
def authenticate(username, password): 
    response = dict()
    response['status'] = 200
    user_details = driver.get_details(username)
    response['response'] = dict()
    response['response']['name'] = user_details['name']
    response['response']['username'] = user_details['username']
    if user_details['password'] == password:
        response['response']['authenticate'] = True
    else:
        response['response']['authenticate'] = False
    response['error'] = None
    return response

'''
function to create a new user 
given the name, date of birth, username and password
'''
def register(data): 
    response = dict()
    response['status'] = 200
    response['response'] = dict()
    response['response']['status'] = driver.add_user(name=data['name'], date_of_birth=data['dob'], username=data['username'], password=data['password'])
    response['error'] = None

'''
function to check if the user with a specific username already exist
'''
def check_user(username): 
    response = dict()
    response['status'] = 200
    response = dict()
    if driver.get_details(username)['name'] is None:
        response['response']['exists'] = False
    else:
        response['response']['exists'] = True
    response['error'] = None
    return response

'''
function to get the list of transactions from the database
starting from offset and limiting number of records to limit 
'''
def get_transactions(user, offset, limit): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_transactions(user, offset, limit)
    response['error'] = None
    return response

'''
function to add a transaction record for the user
'''
def add_transaction(user, data): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.add_transaction(user, date=data['date'], type=data['type'], category=data['category'], dealer=data['dealer'], status=data['status'])
    response['error'] = None
    return response

'''
function to delete a transaction record for a user given the id
'''
def delete_transaction(user, doc_id): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.delete_transaction(user, doc_id)
    response['error'] = None
    return response

'''
function to get a specific transaction record given the id
'''
def get_transaction_by_id(user, doc_id): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_tansaction_by_id(user, doc_id)
    response['error'] = None
    return response
    
'''
function to update the transaction given the new data
'''
def update_transactions(user, data): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.update_transactions(user, doc_id=data['id'], date=data['date'], type=data['type'], category=data['category'], dealer=data['dealer'], status=data['status'])
    response['erorr'] = None
    return response

'''
function to get the debt list
starting from the offset and limiting the number of output records to limit
'''
def get_debt_list(user, offset, limit): 
    response = dict() 
    response['status'] = 200
    response['response'] = driver.get_debt_list(user, offset, limit)
    response['error'] = None
    return response

'''
function to update the status of specified debt list by id
'''
def update_debt_list(user, id_list): 
    response = dict()
    response['status'] = 200
    count = 0
    for doc_id in id_list:
        count += driver.update_debt(user, doc_id)
    response['response'] = count
    response['error'] = None
    return response

'''
function to get the owe list
starting from the offset and limiting the number of output records to limit 
'''
def get_owe_list(user, offset, limit): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_owe_list(user, offset, limit)
    response['error'] = None
    return response

'''
function to update the status of specified owe list by id
'''
def update_owe_list(user, offset, limit): 
    response = dict()
    response['status'] = 200
    count = 0
    for doc_id in id_list:
        count += driver.update_owe_list(user, offset, limit)
    response['response'] = count
    response['error'] = None
    return response

'''
function to get the list of unique categories for a user
'''
def get_all_categories(user): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_all_categories(user)
    response['error'] = None
    return response

'''
function to get summary data by category for a user
'''
def get_summary_by_category(user): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_summary_by_category(user)
    response['error'] = None
    return response

'''
function to get summary data by weekdays for a user
'''
def get_summary_by_weekdays(user): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_summary_by_weekdays(user)
    response['error'] = None
    return response

'''
function to get credit transactions 
starting from the offset and limiting the number of output records to limit 
'''
def get_credit_transactions(user, offset, limit): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_credit_transactions(user, offset, limit)
    response['error'] = None
    return response

'''
function to get debit transactions
starting from the offset and limiting the number of output records to limit 
'''
def get_debit_transactions(user, offset, limit): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_debit_transactions(user, offset, limit)
    response['error'] = None
    return response

'''
function to get save type transactions 
starting from the offset and limiting the number of output records to limit 
'''
def get_saved_transactions(user, offset, limit): 
    response = dict()
    response['status'] = 200
    response['response'] = driver.get_saved_transactions(user, offset, limit)
    response['error'] = None
    return response