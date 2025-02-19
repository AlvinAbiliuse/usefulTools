import os
import sys
import shutil
import random

def move(location):
    paths = os.listdir(f"./{location}");
    p = paths[random.randint(0, len(paths))]
    shutil.copy(f"./{location}/{p}", "./")


def copy(argv):
    print(argv)
    if int(argv[1]) < len(os.listdir(f"./{argv[2]}")):
        for i in range(len(os.lisrdir(f"./{argv[2]}"))):
            move(argv[2])
    else:
        for i in range(int(argv[1])):
            move(argv[2])

copy(sys.argv)

