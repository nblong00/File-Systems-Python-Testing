import os

path = input("Provide path: ")
root =  input("Provie root: ")

def absolute(path, root):
    if not os.path.isabs(path):
        fixed_path = os.path.join(root, path)
        if not os.path.isabs(fixed_path):
            print("\nPath and root provided cannot be combined to make absolute path. Try again...")
            return fixed_path
        print("\nThis is fixed!")
        return fixed_path
    print("\nThe path is already absolute...")
    return path

print("Output path: " + absolute(path, root))
input("\nPress ENTER to close program...")
