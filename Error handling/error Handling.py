# Let the python keep running even if there are errors. 

# try except : catching errors
# except block runs only once and as soon as an error is caught next except blocks wont run even for same error.
# diff except blocks for diff types of error can be made

while True:
    try:
        age = int(input('Enter your age please'))
        print(20/age)
        # break
    except ZeroDivisionError:
        print('Age must be above zero')
    except ValueError:
        print('Invalid entry')
    except ValueError:
        print('!!!!')
    else:
        print('Thank you')
        break

