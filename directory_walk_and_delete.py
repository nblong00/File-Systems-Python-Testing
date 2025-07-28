from pathlib import Path


def remove_dir(path):
    path.rmdir()


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
            remove_dir(joined_path)


def app():
    user_input = input('Enter the absolute or relative path: ')
    path = Path(user_input)
    directory_walk_and_delete(path)


app()
