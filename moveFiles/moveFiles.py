import os
import sys
import shutil
import random

def copy(argv):
    print(argv)
    for i in range(int(argv[1])):
        paths = os.listdir(f"./{argv[2]}");
        p = paths[random.randint(0, len(paths))]
        shutil.copy(f"./{argv[2]}/{p}", "./")

copy(sys.argv)

