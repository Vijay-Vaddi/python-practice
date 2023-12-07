import sys
import PyPDF2

inputs = sys.argv[1:]

print(inputs)
#loop through pages
# merge/add watermaker to each pages
# append pages to writer object
# save final result 

#read input file into a read object
#read input watermark into read object

def pdf_watermarker(files):
    reader_file = PyPDF2.PdfReader(files[0])
    reader_mark = PyPDF2.PdfReader(files[1])
    
    writer = PyPDF2.PdfWriter()

    for page_num in range(len(reader_file.pages)):
        page = reader_file.pages[page_num]
        page.merge_page(reader_mark.pages[0])
        writer.add_page(page)
            
    with open('watermarked.pdf', 'wb') as new_file:
        writer.write(new_file)


pdf_watermarker(inputs) 