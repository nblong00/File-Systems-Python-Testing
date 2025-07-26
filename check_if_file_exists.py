import os
from datetime import datetime


def timestamp_convert(path, name):
    timestamp = os.path.getatime(os.path.join(path, name))
    converted_timestamp = datetime.fromtimestamp(timestamp)
    dt = datetime.strftime(converted_timestamp, "%m-%d-%Y at %I:%m %p")
    return dt


def dir_contains():
    path = input('Enter relative or absolute path: ')
    for name in os.listdir(path):
        dt = timestamp_convert(path, name)
        if os.path.isdir(os.path.join(path, name)):
            print(f"\nDirectory Name: {name}")
            print(f"Last accessed: {dt}")
            print("Directory located at "+ (os.path.join(path, name)))
        else:
            print(f"\nFile Name: {name}")
            print(f"Last accessed: {dt}")
            print("File located at " + (os.path.join(path, name)))
    print()


dir_contains()
