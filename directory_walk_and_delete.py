from pathlib import Path


def joined_path_creator(path, item):
    joined_path = Path(path / item)
    return joined_path


def directory_walk_and_delete(path):
    for root, dirs, files in Path(path).walk(top_down=False):
        for item in files:
            joined_path = joined_path_creator(root, item)
            joined_path.unlink()
        for folder in dirs:
            joined_path = joined_path_creator(root, folder)
            joined_path.rmdir()


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


def app():
    while True:
        path = check_if_entry_is_valid()
        if path == "main-menu":
            continue
        path = check_if_directory_is_empty(path)
        if path == "main-menu":
            continue
        sort_directory_contents(path)
        directory_walk_and_delete(path)


if __name__ == "__main__":
    app()
