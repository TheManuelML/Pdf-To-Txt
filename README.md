# PDF to Plain text
This script transform PDF files into plain text ones. It also have a recursive function for you to give a directory full of PDF files. The script do not use OCR.

## Usage
```
>>> python3 pdf_to_text.py -p ./Path/To/File.pdf -r ./txt/result
Or
>>> python3 pdf_to_text.py -p .\\Path\\To\\Directory\\ -r .\\txt\\results\\
```

## Flags
- -p -> Add a path to a PDF file or a directory with PDFs
- -r -> Add a path to a directory where you want to store the plain text files (optional) 
