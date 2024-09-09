import os
import shutil
import json
from sys import argv

library = None

def fun(dir, head, floor):
    entries = os.scandir(dir)
    for entry in entries:
        if entry.is_file():
            new_name = entry.path[:head]+entry.path[head:].replace("\\", "_").replace("/", "_")
            if new_name != entry.path:
                if not os.path.exists(new_name):
                    if entry.path in library:
                        print("File %s has been renamed. Skipped."%(entry.path))
                    else:
                        print("Rename %s to %s."%(entry.path, new_name))
                        os.rename(entry.path, new_name)
                        library[new_name] = entry.path
                else:
                    print("File %s has existed. Skipped." % new_name)
        else:
            fun(dir+"\\"+entry.name, head+(len(entry.name)+1 if floor>0 else 0), floor-1)
            if floor<=0:
                try:
                    os.rmdir(entry.path)
                except:
                    pass

try:
    with open(".rename_lib", "r") as f:
        library = json.load(f)
        f.close()
    print("Found rename library.")
except:
    print("Create a new rename library.")
    library = dict()

floor = input("floor:")
if floor == "":
    floor = 0
else:
    floor = int(floor)
fun(".", 2, floor)

with open(".rename_lib", "w") as f:
    json.dump(library, f)
    f.close()

input("Press any key to exit.")