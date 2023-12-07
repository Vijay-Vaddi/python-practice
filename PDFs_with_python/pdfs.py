import PyPDF2

#rb for reading binary files. 
with open('./PDFs_with_python/dummy.pdf', 'rb') as file:
    
    # print(file)
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    print(reader.pages[0])
    
    # get a single single page object 
    page = reader.pages[0]
    print(page.rotate(90))
    

    #need to write to a pdf file object and save
    write_pdf = PyPDF2.PdfWriter() #new writer object
    write_pdf.add_page(page)
    #upto now the rotated page is added to the writer object and not to the file. 

    with open('./PDFs_with_python/tilted.pdf', 'wb') as new_file:
        write_pdf.write(new_file)
    
    #tilted pdf is a new empty pdf  object, you perform write function by passing new_file/tilted to it.          

    
    




'''
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()
 
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
 
    with open('watermarked.pdf', 'wb') as file:
        output.write(file)

'''