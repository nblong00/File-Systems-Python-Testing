import os
import time

path = input('Enter relative or absolute path: ')


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


def dir_contains(path, filenames):
    for name in filenames:
        if name not in os.listdir(path):
            print(f"{name} is not a file within the supplied directory...")
            input("Press ENTER to close program...")
            return False
    return True


print(dir_contains(path, file_input()))
