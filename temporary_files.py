import os
import tempfile

with tempfile.TemporaryDirectory() as tempdirname:
    print(f"Created temporary directory named {tempdirname}")
    with open(os.path.join(tempdirname, 'temporary_file.txt'), 'w') as f:
        f.write("This is a temporary file...")
    input()