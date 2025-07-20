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


FILES = {
    '{project_slug}/requirements.txt': 'requiements.txt.template',
    '{project_slug}/app.py': 'app.py.template',
    '{project_slug}/static/css/{project_slug}.css': 'project.css.template',
    '{project_slug}/static/js/{project_slug}.js': 'project.js.template',
    '{project_slug}/template/index.html': 'project.html.template'
}


def flask_template_prepare(string):
    string = re.sub(r'\{\%', '<%', string)
    string = re.sub(r'\%\}', '%>', string)
    string = re.sub(r'\{\{', '<<', string)
    string = re.sub(r'\}\}', '>>', string)
    return string


def flask_template_repair(string):
    string = re.sub(r'\<\%', '{%', string)
    string = re.sub(r'\%\>', '%}', string)
    string = re.sub(r'\<\<', '{{', string)
    string = re.sub(r'\>\>', '}}', string)
    return string


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


def create_files(root, slug, name):
    for file_name, template_name in FILES.items():
        try:
            template_file = open(os.path.join('templates', template_name))
            file_content = template_file.read()
            file_content = flask_template_prepare(file_content)
            file_content = file_content.format(project_name=name, project_slug=slug)
            file_content = flask_template_repair(file_content)

            target_file = open(os.path.join(root, file_name.format(project_slug=slug)), 'w')
            target_file.write(file_content)
        except OSError:
            print(f"Could created {file_name.format(project_slug=slug)}")
        # finally:
        #     template_file.close()
        #     target_file.close()


def main():
    project_root = get_root()
    check_delete_root(project_root)
    project_name = None
    while not project_name:
        project_name = input("What is full name of project? ").strip()
    project_slug = slugify(project_name)
    create_dirs(project_root, project_slug)
    create_files(project_root, project_slug, project_name)
    print(f"Creating {project_name} in {project_root}")


if __name__ == '__main__':
    main()
