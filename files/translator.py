from translate import Translator

try:
    with open('files/English.txt', mode='r') as my_file:
        translator = Translator(to_lang='ja', from_lang='en') 
        translation = translator.translate(my_file.read())
        print(translation)
        with open('files/Japanese.txt', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as error1:
    print('File Not Found')
except IOError as error2:
    print('IO Error')

