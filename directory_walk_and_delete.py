from pathlib import Path
import time


def joined_path_creator(path, item):
    joined_path = Path(path / item)
    return joined_path


def check_if_entry_is_valid():
    user_input = input("Enter the absolute or relative path: ")
    path = Path(user_input)
    if path.exists() == True:
        if path.is_dir() == False:
            print("Invalid... Entry needs to be a directory...")
            input("Press Enter to try again...")
            return "main-menu"
        return path
    else:
        print("Entry invalid... Input needs to exist and be a directory...")
        input("Press Enter to try again...")
        return "main-menu"


def check_if_directory_is_empty(path):
    files = [item for item in path.iterdir() if item.is_file()]
    directories = [item for item in path.iterdir() if item.is_dir()]
    if not files and not directories:
        print("Invalid... Directory is empty...")
        input("Press Enter to try again...")
        return "main-menu"
    return path


def sort_directory_contents(path):
    items = []
    folders = []
    for root, dirs, files in Path(path).walk():
        for item in files:
            items.append(item)
        for folder in dirs:
            folders.append(folder)
    return items, folders


def print_directory_contents(items, folders):
    item_count = len(items)
    folder_count = len(folders)
    print("\nThis path currently contains-")
    print(f"\nFiles({item_count}):")
    for item in items:
        print(item)
    print(f"\nDirectories({folder_count}):")
    for folder in folders:
        print(folder)
    print()


def ask_user_to_confirm_deletion():
    print("Please confirm you want to delete the above items (yes/no):")
    while True:
        user_input = input("> ")
        if user_input in ["yes", "ye", "y"]:
            time.sleep(0.5)
            print("""
                  \r--------------------
                  \rCONTENTS DELETED!
                  \r--------------------
                  """)
            time.sleep(0.5)
            return True
        elif user_input in ["no", "n"]:
            print("\nReturning to main-menu...\n")
            return "main-menu"
        elif user_input not in ["yes", "ye", "y", "no", "n"]:
            print("\nInvalid Entry... Enter either 'yes' or 'no' to the previous question...\n")


def ask_if_user_wants_to_run_program_again():
    print("Would you like to delete another directory's contents (yes/no):")
    while True:
        user_input = input("> ")
        if user_input in ["yes", "ye", "y"]:
            print("\nReturning to main-menu...\n")
            break
        elif user_input in ["no", "n"]:
            exit()
        elif user_input not in ["yes", "ye", "y", "no", "n"]:
            print("\nInvalid Entry... Enter either 'yes' or 'no' to the previous question...\n")


def directory_walk_and_delete(path):
    for root, dirs, files in Path(path).walk(top_down=False):
        for item in files:
            joined_path = joined_path_creator(root, item)
            joined_path.unlink()
        for folder in dirs:
            joined_path = joined_path_creator(root, folder)
            joined_path.rmdir()


def app():
    while True:
        path = check_if_entry_is_valid()
        if path == "main-menu":
            continue
        path = check_if_directory_is_empty(path)
        if path == "main-menu":
            continue
        (items, folders) = sort_directory_contents(path)
        print_directory_contents(items, folders)
        exit_choice = ask_user_to_confirm_deletion()
        if exit_choice == "main-menu":
            continue
        directory_walk_and_delete(path)
        ask_if_user_wants_to_run_program_again()


if __name__ == "__main__":
    app()
