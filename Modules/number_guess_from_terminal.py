from random import randint
from random import randrange
import sys

# answer = randint(int(sys.argv[1]), int(sys.argv[2]))
answer = randrange(int(sys.argv[1]), int(sys.argv[2]))
# randrange did not work from terminal

while True:
    try:
        guess = int(input(f'Please enter a number from 1 to 10 '))
        if  0< guess <11:
            if guess == answer:
                print(f'Hurrah... You win but its nothing!!!')
                break
            else:
                print(f'wrong guess, tough luck!! Lets try that again ')
                continue
        else:
            print(f'Its not 1-10 bro')
            continue
    except ValueError:
        print('That is not a number man')
        continue

