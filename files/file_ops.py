my_file = open('test.txt')


# print(my_file.read()) #reads once and cursor will move to the end of the line. 
# my_file.seek(0) #moves the cursor back to 0
# print(my_file.read())
# print(my_file.read())

# print(my_file.readline()) 
# print(my_file.readline())
# print(my_file.readline())

print(my_file.readlines()) #can use reg ex to search for something in a file. 

my_file.close() #good standard to close. 