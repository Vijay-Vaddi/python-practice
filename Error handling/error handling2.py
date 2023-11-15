def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as error:
        print(f'Error: {error}')

print(sum(2,'3'))   