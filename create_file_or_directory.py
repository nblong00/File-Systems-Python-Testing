import os

file_name = input("File name: ")
new_directory = input("New directory name: ")
os.mkdir(new_directory)
absolute_path = os.path.join(os.getcwd(), new_directory)
print(absolute_path)
input("Press ENTER to write file in newly created directory...")
with open(os.path.join(absolute_path, file_name), 'w') as file:
    file.write("Wow, we created a file!")
    input("Press ENTER to close file...")
