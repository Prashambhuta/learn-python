#! usr/bin/env python3

"""
Changing the styles of the document
"""

import docx

# def document and paragraph object
doc_object = docx.Document('other/demo.docx')
par_object = doc_object.paragraphs

# check the paragraph style
print(par_object[1].style)

# change the paragraph style to 'Title'
par_object[1].style = "Subtitle"

doc_object.save('other/demo.docx')