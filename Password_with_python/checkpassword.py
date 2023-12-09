import requests

#send first 5 chars of hashed password123 as request to api to compare with database
url = 'https://api.pwnedpasswords.com/range/' + 'cbfda'

res = requests.get(url)
print(res) 

def request_api_data(query_data):
    pass

def pawned_api_check(password):
    pass

