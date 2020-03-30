#! usr/bin/env python3

"""
READING & EDITING .pdf FILES IN PYTHON using 3rd party module - PyPDF2
"""

import PyPDF2
import os

os.chdir('other')

# call the python open function with arg 'rb' to open in 'read-binary'
# .pdf are by default binary files
pdf_file = open('meetingminutes1.pdf', 'rb')

# passing the pdf_file object to reader fn in PyPDF2
file_reader = PyPDF2.PdfFileReader(pdf_file)

# to check number of pages in a document
print(file_reader.numPages)

# method .getPage will return a page_object
page_1 = file_reader.getPage(0)

# extract text contain using .extractText() method
print(page_1.extractText())

# extract text from all the pages
for page_num in range(file_reader.numPages):
    page_object = file_reader.getPage(page_num)
    print(page_object.extractText())

"""
PyPDF2 only works on page level. It is difficult to add, edit text in pdf.
You can however add pages, merge pages from other pdfs, 
"""

# example: merge 2 pdfs from '/other' folder

# create two file objects for two files
pdf_file1 = pdf_file    # where pdf_file is defined earlier
pdf_file2 = open('meetingminutes2.pdf', 'rb')

# create 2 reader objects, one for each file
pdf1_reader = PyPDF2.PdfFileReader(pdf_file1)
pdf2_reader = PyPDF2.PdfFileReader(pdf_file2)

""" 
Create a new pdf using PyPDF2
"""

# create a pdf writer object using .PdfFileWriter() method
pdf_writer = PyPDF2.PdfFileWriter()

# adding pages at end using .addPage() method

# adding pages from pdf_1 using for loop
for page_num in range(pdf1_reader.getNumPages()):
    page_object = pdf1_reader.getPage(page_num)
    pdf_writer.addPage(page_object)

# adding pages from pdf_2 using for loop
for page_num in range(pdf2_reader.getNumPages()):
    page_object = pdf2_reader.getPage(page_num)
    pdf_writer.addPage(page_object)

# using open function to create a new pdf file

# create a output file object in write-binary ('wb') mode
merged_pdf_object = open('merged_meetingminutes.pdf', 'wb')

# using the write method on write function to save the output file
pdf_writer.write(merged_pdf_object)

# close all open files
merged_pdf_object.close()
pdf_file2.close()
pdf_file1.close()
