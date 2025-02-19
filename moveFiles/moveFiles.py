import os
import sys
import shutil
import random

def move(argv):
    paths = os.listdir(f"./{argv[2]}");
    p = paths[random.randint(0, len(paths))]
    shutil.copy(f"./{argv[2]}/{p}", "./")


def copy(argv):
    print(argv)
    if int(argv[1]) < len(os.listdir(f"./{argv[2]}")):
        for i in range(len(os.lisrdir(f"./{argv[2]}"))):
            move(argv[2])
    elif:
        for i in range(int(argv[1])):
            move(argv[2])

copy(sys.argv)

