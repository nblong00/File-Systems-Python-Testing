import os


def showcase_files_in_current_directory(path):
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)) == True:
            print(f'{item} is a file!')
        else: 
            print(f'{item} is a directory...')


def sort_files_in_lower_directories(path):
    items = [item for root, dirs, files in os.walk(path) for item in files]
    folders = [folder for root, dirs, files in os.walk(path) for folder in dirs]
    return items, folders


def showcase_files_in_lower_directories(items, folders):
    print("\nFolders in lower directories:\n")
    for folder in folders:
        print(folder)
    print("\nFiles in lower directories:\n")
    for item in items:
        print(item)
    print()


def menu_after_original_showcase(path):
    while True:
        print("""
            \rChoose one of the below numbered options:
            \r1) Explore lower directories
            \r2) Close program...
            """)
        menu_decision = input("> ")
        if menu_decision == '1':
            (items, folders) = sort_files_in_lower_directories(path)
            showcase_files_in_lower_directories(items, folders)
            input("Press ENTER to close program...")
            break
        elif menu_decision == '2':
            exit()
        elif menu_decision not in ['1', '2']:
            print('Invalid entry. Either enter the number 1 or 2.')
            continue


def main():
    path = '..\\..\\ExploringGIT\\pythontesting'
    showcase_files_in_current_directory(path)
    menu_after_original_showcase(path)


if __name__ == "__main__":
    main()
