import os

string = 'fourth'

def delete_by_date(string):
    for thing in os.scandir('../../../pythontesting/container'):
        if string in thing.name:
            os.remove(thing)

delete_by_date(string)
