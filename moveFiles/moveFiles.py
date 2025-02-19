import os
import sys
import shutil
import random

def copy(argv):
    print(argv)
    for i in range(argv[1]):
        paths = os.listdir(f"./{argv[2]}");
        print(random.randint(0, len(paths)))


copy(sys.argv)

