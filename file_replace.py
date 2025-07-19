import os
import re

path = '../../../pythontesting'


def cleanup(path):
    for entry in os.listdir(path):
        split_path = re.split(r'[.-]+', entry)
        # Looking for file named similar to jamescampbell2-2012-04-29.txt
        name_format = split_path[1] + '-' + split_path[2] + '-' + split_path[3] + '-' + split_path[0] + '.' + split_path[4]
        os.replace(os.path.join(path, entry), os.path.join(path, name_format))


cleanup(path)
