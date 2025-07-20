import os
import time


def file_input():
    files = []
    while True:
        file_name = input('Enter file (with extension) to check if it exists in previously mentioned path: ')
        time.sleep(0.5)
        files.append(file_name)
        add_another = input("Would you like to add another file to the check? (y/n) ")
        if add_another in ['yes', 'ye', 'y']:
            continue
        else:
            return files


def dir_contains(filenames):
    path = input('Enter relative or absolute path: ')
    for name in filenames:
        if name not in os.listdir(path):
            print(f"{name} is not a file or directory within the supplied path...")
    input("Press ENTER to close program...")


dir_contains(file_input())
