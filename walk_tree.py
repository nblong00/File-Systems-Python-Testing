import os


def showcase_files_in_current_directory(path):
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)) == True:
            print(f'{item} is a file!')
        else: 
            print(f'{item} is a directory...')


def menu_after_original_showcase(path):
    while True:
        print("""
            \rChoose one of the below numbered options:
            \r1) Explore lower directories
            \r2) Close program...
            """)
        menu_decision = input("> ")
        if menu_decision == '1':
            pass
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
