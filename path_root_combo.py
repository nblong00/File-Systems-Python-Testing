import os


def gather_user_input():
    path = input("Provide path: ")
    root =  input("Provie root: ")
    return path, root


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


def output_absolute_path(path, root):
    print("Output path: " + absolute(path, root))
    input("\nPress ENTER to close program...")


def main():
    (path, root) = gather_user_input()
    output_absolute_path(path, root)


if __name__ == "__main__":
    main()
