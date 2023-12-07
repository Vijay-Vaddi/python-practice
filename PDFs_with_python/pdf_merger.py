import PyPDF2
import sys

inputs = sys.argv[1:] #captures all the inputs

def pdf_merger(pdf_list):
    #create merger object
    merger = PyPDF2.PdfMerger()
    #merger object methods works only on pdfs and assumes all itputs are pdfs.
    # wont work otherwise. gives PyPDF2.errors.PdfReadError: 
    
    for pdf in pdf_list:
        
        merger.append(pdf)
    merger.write('merged_file.pdf')

  
pdf_merger(inputs)

