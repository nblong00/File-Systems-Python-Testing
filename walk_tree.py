import os

PATH = '..\\..\\ExploringGIT\\pythontesting'

for item in os.listdir(PATH):
    if '.' in item:
        file_test = os.path.isfile(os.path.join(PATH, item))
        print(f'This is a file: {file_test}')
    else: 
        print(f'This is a directory... [{item}]')
