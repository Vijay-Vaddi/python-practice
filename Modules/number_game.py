import sys
secret = 7
while True:
    
    print(f'Please guess a number between 1 and 10') 
    guess = input()
    if guess == secret:
        print(f'Congrats!!!')
        break

    