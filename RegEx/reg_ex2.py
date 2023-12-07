# can think of RegEx as a entire language itself. 
# regex101.com
# https://regexone.com/
# used for validation. email, username etc

import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# while True:
    # email_id = input('Enter your email Id')
    # if email_id == 
email_id = '420@69.com'
a = pattern.search(email_id)
print(a)
