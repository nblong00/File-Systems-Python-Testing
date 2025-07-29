import os
import tempfile


def write_temp_file():
    with tempfile.TemporaryDirectory() as tempdirname:
        print(f"Created temporary directory named {tempdirname}")
        with open(os.path.join(tempdirname, "temporary_file.txt"), "w") as f:
            f.write("This is a temporary file...")
        input()

def main():
    write_temp_file()

if __name__ == "__main__":
    main()