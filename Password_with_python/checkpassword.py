import requests
import hashlib 

#send first 5 chars of hashed password123 as request to api to compare with database

def request_api_data(query_data):
    url = 'https://api.pwnedpasswords.com/range/' + query_data
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code}, check API please')
    return res


def pawned_api_check(password):
    
    #encode password into utf-8 string, 
    # use sha1 to hash it, gives sha1 object
    #digest to return hex value. 
    # turn to upper case to match with API
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1password)

    print(request_api_data(sha1password[:5]))

pawned_api_check('123')
