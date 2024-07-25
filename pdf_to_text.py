### Created by Manuel Magaña López [TheManuelML], look at my GitHub profile: https://github.com/TheManuelML
### USAGE: The script have two modes; Recursive that works with directories, and Single that works with a file.
### For each option write either the path to the file or the path to the directory, if you are on Windows use
### double backslash to avoid interpreter problems, example: python exec.py -f ".\\Data\\MyPdfs\\Example.pdf"
### or python exec.py -d ".\\Data\\MyPdfs\\".

import os
import sys
import argparse
import fitz #Helps us to open and read PDF files

# Arguments
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-p', '--path') # Path to a directory full of PDFs
parser.add_argument('-r', '--results') # Path to a directory where the TXT is going to be store
argument = parser.parse_args()

# Processing functions
## File processing
def file_processing(file_path : str, results_path : str) -> None:
    pdf_name = os.path.basename(file_path)
    txt_name = pdf_name[:-4] + '.txt'

    txt_path = os.path.join(results_path, txt_name)
    pdf_to_txt(file_path, txt_path)
    return None

## Directory processing
def dir_processing(directory_path : str, results_path : str) -> None:
    with os.scandir(directory_path) as first_level:
        for element in first_level:
            if os.path.isdir(element.path):
                recursive(element.path, results_path)
            elif os.path.isfile(element.path) and element.name.endswith('.pdf'):
                file_processing(element.path, results_path)
    return None

## Recursive
def recursive(directory_path : str, results_path : str):
    for element in os.listdir(directory_path):
        full_path = os.path.join(directory_path, element)
        if os.path.isdir(full_path):
            recursive(full_path, results_path)
        else:
            file_processing(full_path, results_path)
    return None

# From PDF to plain text
def pdf_to_txt(file_path : str, result_path : str) -> None:
    document = fitz.open(file_path)
    text = ''
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    with open(result_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    print(f'File {os.path.basename(file_path)} sucessfully converted to TXT')
    return None

# Main function
def main() -> None:
    ## Directory where the TXT files are going to be store
    try:
        os.path.isdir(argument.results)
    except TypeError:
        print('The results path directory is not a valid PATH!!!')
        sys.exit(1)

    ## Directory with PDFs path or path to a PDF file
    if os.path.isfile(argument.path):
        pdf_path = argument.path
        file_processing(pdf_path, argument.results)
    elif os.path.isdir(argument.path):
        dir_path = argument.path
        dir_processing(dir_path, argument.results)
    else:
        print('It is necessary a directory or a file path!!!')
        sys.exit(1)
    return None


if __name__ == '__main__':
    main()
