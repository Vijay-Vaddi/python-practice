def greeting():
    print(f'Hello there')

user = {
    'age' : 30,
    'name': 'Obi-Wan Kenobi',
    'magic': True,
    'greeting': greeting
}

#all O(1)
user['greeting']()
print(user['age'])


