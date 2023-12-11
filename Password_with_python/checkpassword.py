import requests
import hashlib 
import sys

def request_api_data(query_data):
    url = 'https://api.pwnedpasswords.com/range/' + query_data
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code}, check API please')
    return res

def password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pawned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_chars, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_5_chars)
    return password_leaks_count(response, tail)


def main(passwords):
    for password in passwords:
        count = pawned_api_check(password)
        if count:
            print(f'{password} was hacked {count} times dowg, try something else')
        else:
            print(f'{password} seem to be unhackable so far, right this way my leigh')
    return 'DONE'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
