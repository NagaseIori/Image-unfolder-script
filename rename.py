import os
import shutil
from sys import argv

def fun(dir):
    entries = os.scandir(dir)
    for entry in entries:
        if entry.is_file():
            new_name = entry.path[2:].replace("_", "-U").replace("\\", "_").replace("/", "_")
            os.rename(entry.path, "./"+new_name)
        else:
            fun(dir+"/"+entry.name)
            os.rmdir(entry.path)

fun(".")
os.remove(argv[0])
