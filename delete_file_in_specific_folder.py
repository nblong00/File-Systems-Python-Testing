import os


def delete_by_date():
    string = 'fourth'
    for thing in os.scandir('../../../pythontesting/container'):
        if string in thing.name:
            os.remove(thing)


def main():
    delete_by_date()


if __name__ == "__main__":
    main()
