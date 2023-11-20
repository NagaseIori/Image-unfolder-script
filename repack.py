from genericpath import exists
import os
import json
import shutil
from sys import argv

entries = os.scandir(".")
library = None

try:
    with open(".rename_lib", "r") as f:
        library = json.load(f)
        f.close()
    print("Found rename library.")
    print(library)
except:
    library = None
    print("Library not found. Fallback to classic methods.")

for entry in entries:
    if entry.is_file():
        new_path = entry.path
        if library == None:
            nlist = list(new_path)
            if(new_path.rfind("_") == -1 and new_path.rfind("-U") == -1):
                continue
            if new_path.rfind("_") !=-1:
                nlist[new_path.rfind("_")] = '\\'
            new_path = ''.join(nlist) ;
            new_path = new_path.replace("_", "/").replace("-U", "_");
        else:
            if entry.path in library:
                new_path = library[entry.path]
            else:
                print(f"{entry.path} not in library file. Skip.")
        # print(new_path[0:new_path.rfind("\\")]);
        print("Rename %s to %s" % (entry.path, new_path))
        if entry.path.rfind("_")!=-1:
            if not os.path.exists(new_path[0:new_path.rfind("\\")]):
                os.makedirs(new_path[0:new_path.rfind("\\")])
        if not os.path.exists(new_path):
            os.rename(entry.path, new_path)
        else:
            print("File %s has existed. Skip." % new_path)
            # os.remove(entry.path)

print("Press anykey to continue.")
input()

os.remove(".rename_lib")
os.remove(argv[0])
