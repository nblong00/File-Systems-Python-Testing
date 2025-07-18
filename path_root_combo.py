import os

path = input("Provide path: ")
root =  input("Provie root: ")

def absolute(path, root):
    if not os.path.isabs(path):
        fixed_path = os.path.join(root, path)
        return fixed_path
    return path

print(absolute(path, root))