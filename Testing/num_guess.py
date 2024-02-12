from random import randint
from random import randrange
import sys


# answer = randrange(int(sys.argv[1]), int(sys.argv[2]))
# randrange did not work from terminal
def guess_num(guess, answer):
    print('hii')
    try:
        if  0< guess <11:
            if guess == answer:
                print(f'Hurrah... You win but its nothing!!!')
                return True
            else:
                print(f'wrong guess, tough luck!! Lets try that again')
                return False
        else:
            print( f'Its not 1-10 bro')
            return False
    except TypeError as err:
        print('wrong type')
        return 'TypeError'

if  __name__ == '__main__':
    answer = randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            guess = int(input(f'Please enter a number from 1 to 10 '))
            
            if (guess_num(guess, answer)):
                break
             
        except ValueError as err:
            print('that is not a number')
            # continue

