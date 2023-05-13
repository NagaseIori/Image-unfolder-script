from genericpath import exists
import os
import shutil

entries = os.scandir(".")

for entry in entries:
    if entry.is_file():
        new_path = entry.path
        nlist = list(new_path)
        if(new_path.rfind("_") == -1 and new_path.rfind("-U") == -1):
            continue
        if new_path.rfind("_") !=-1:
            nlist[new_path.rfind("_")] = '\\'
        new_path = ''.join(nlist) ;
        new_path = new_path.replace("_", "/").replace("-U", "_");
        # print(new_path[0:new_path.rfind("\\")]);
        print("Rename %s to %s" % (entry.path, new_path))
        if entry.path.rfind("_")!=-1:
            if not os.path.exists(new_path[0:new_path.rfind("\\")]):
                os.makedirs(new_path[0:new_path.rfind("\\")])
        if not os.path.exists(new_path):
            os.rename(entry.path, new_path)
        else:
            print("File %s has existed. Skipped." % new_path)
            # os.remove(entry.path)

input()