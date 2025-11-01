#-------------------------------------------------------------------------------
# Name:        PDF to Docuement Converter
# Purpose:     Python code used to convert PDF to Document using pdf2docx
#
# Author:      Mithun Vishwakarmq
#
# Created:     21/09/2022
# Copyright:
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pdf2docx import Converter

# Provide path of your pdf file

pdf = 'C:\Training\Python Practice\Python Example\DocumentFile\SampleFile.pdf'

#provide path where you save document file

document_file='C:\Training\Python Practice\Python Example\DocumentFile\ConvertedDocument.docx'

obj = Converter(pdf)
obj.convert(document_file)
obj.close()
