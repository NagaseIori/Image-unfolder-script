from genericpath import exists
import os
import shutil

entries = os.scandir(".")

for entry in entries:
    if entry.is_file():
        new_path = entry.path
        nlist = list(new_path)
        if(new_path.rfind("_") == -1):
            continue
        nlist[new_path.rfind("_")] = '\\'
        new_path = ''.join(nlist) ;
        new_path = new_path.replace("_", "/").replace("__", "_");
        # print(new_path[0:new_path.rfind("\\")]);
        if not os.path.exists(new_path[0:new_path.rfind("\\")]):
            os.makedirs(new_path[0:new_path.rfind("\\")])
        os.rename(entry.path, new_path)
