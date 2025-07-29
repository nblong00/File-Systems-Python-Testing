import os


def gather_user_input():
    file_name = input("File name: ")
    new_directory = input("New directory name: ")
    return file_name, new_directory


def make_directory(new_directory):
    os.mkdir(new_directory)


def absolute_path_for_directory(new_directory):
    absolute_path = os.path.join(os.getcwd(), new_directory)
    print(absolute_path)
    return absolute_path


def write_to_new_file(absolute_path, file_name):
    input("Press ENTER to write file in newly created directory...")
    with open(os.path.join(absolute_path, file_name), 'w') as file:
        file.write("Wow, we created a file in a new directory!")
    input("Press ENTER to close program...")


def main():
    (file_name, new_directory) = gather_user_input()
    make_directory(new_directory)
    absolute_path = absolute_path_for_directory(new_directory)
    write_to_new_file(absolute_path, file_name)


if __name__ == "__main__":
    main()
