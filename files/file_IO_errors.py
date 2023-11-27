try: 
    with open('test.txt', mode='r') as my_file1:
        print(my_file1.readline())

except FileNotFoundError as err:
    print('No such file in this directory bro')
    raise err

except IOError as ioErr:
    print('IO error bro')
    raise ioErr


