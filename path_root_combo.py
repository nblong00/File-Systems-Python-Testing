import os

path = input("Provide path: ")
root =  input("Provie root: ")

def absolute(path, root):
    if not os.path.isabs(path):
        fixed_path = os.path.join(root, path)
        print("This is fixed!")
        return fixed_path
    print("The path is already absolute...")
    return path

print(absolute(path, root))
input("Press ENTER to close program...")
