import unicodedata
import pathlib
import os
import re

DIRS = [
    '{project_slug}/',
    '{project_slug}/static/',
    '{project_slug}/static/img/',
    '{project_slug}/static/js/',
    '{project_slug}/static/css/',
    '{project_slug}/templates/',
]


def slugify(string):
    string = unicodedata.normalize('NFKC', string)
    string = re.sub(r'[^\w\s]', '', string).strip().lower()
    return re.sub(r'[-_\s]+', '_', string)


def get_root():
    root = pathlib.PurePath(
        input("What is the full path to create project at? ")
    )
    if not root.is_absolute():
        return get_root()
    return root


def check_delete_root(root):
    if os.path.exists(root):
        print("Path already exists...")
        try:
            delete = input("Delete existing files/directorie? (y/n)").lower()
            if delete in ['yes', 'ye', 'y']:
                delete = True
        except ValueError:
            return check_delete_root(root)
        else:
            if delete:
                try: 
                    os.removedirs(root)
                except OSError:
                    print(f"Couldn't delete {root}. Please delete it yourself.")
                else:
                    print(f"Deleted {root}")
    return None


def create_dirs(root, slug):
    try:
        os.makedirs(root)
    except OSError:
        print(f"Couldn't create the project root at {root}")
    else:
        for folder in DIRS:
            try:
                os.mkdir(os.path.join(root, folder.format(project_slug=slug)))
            except FileExistsError:
                pass                


def main():
    project_root = get_root()
    check_delete_root(project_root)
    project_name = None
    while not project_name:
        project_name = input("What is full name of project? ").strip()
    project_slug = slugify(project_name)
    create_dirs(project_root, project_slug)
    print(f"Creating {project_name} in {project_root}")


if __name__ == '__main__':
    main()
