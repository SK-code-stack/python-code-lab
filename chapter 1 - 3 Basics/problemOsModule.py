import os

directory_path = '/home/salman/ML Course'

contents = os.listdir(directory_path)

for items in contents:
    print(items)