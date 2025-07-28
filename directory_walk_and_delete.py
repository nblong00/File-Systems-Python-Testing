import os
from pathlib import Path


def remove_dir(path):
    path.rmdir()


def directory_walk_and_delete(path):
    for root, dirs, files in Path(path).walk(top_down=False):
        for item in files:
            fixed_path = Path(os.path.join(root, item))
            fixed_path.unlink()
        for folder in dirs:
            fixed_path = Path(os.path.join(root, folder))
            remove_dir(fixed_path)


def app():
    user_input = input('Enter the absolute or relative path: ')
    path = Path(user_input)
    directory_walk_and_delete(path)
