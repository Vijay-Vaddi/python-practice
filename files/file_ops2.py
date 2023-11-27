# no need to close file with this. 
# built in with statement
# proper way to work with file in python
with open('test.txt', mode='a') as my_file:
    text = my_file.write('General Kenobi')
    print(text) #prints number of characters written to the file. 
    # print(my_file.readlines())

# w : mode creates new file. 