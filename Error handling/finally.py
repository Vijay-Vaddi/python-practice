# finally runs at the end of every try excpect block if the program flows into it without any break. 
# raise can be used to throw a your own error with a message and an except isnt used.  

while True:
    try:
        age = int(input('Enter your age please'))
        # raise ValueError('Hey that\'s no good')
    except ZeroDivisionError:
        print('Age must be above zero')
    except ValueError:
        print('Invalid entry')
    except ValueError:
        print('!!!!')
    else:
        print('Thank you')
        break
    finally:
        print('Thank you. We\'re done here')
    # print('Can you here me?')