import os
import shutil
from sys import argv

def fun(dir, head, floor):
    entries = os.scandir(dir)
    for entry in entries:
        if entry.is_file():
            new_name = entry.path[:head]+entry.path[head:].replace("_", "-U").replace("\\", "_").replace("/", "_")
            print("Rename %s to %s."%(entry.path, new_name))
            if not os.path.exists(new_name):
                os.rename(entry.path, new_name)
            else:
                print("File %s has existed. Skipped." % new_name)
        else:
            fun(dir+"/"+entry.name, head+(len(entry.name)+1 if floor>0 else 0), floor-1)
            if floor<=0:
                os.rmdir(entry.path)

floor = int(input("floor:"))
fun(".", 2, floor)
input("Press any key to exit.")
os.remove(argv[0])