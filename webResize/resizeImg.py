from PIL import Image
import os
import sys

def resize(sizes, path,  destination):
    try:
        os.mkdir(destination)
    except:
        print(f"{destination} folder exists!")

    for i in os.listdir(path):
        try:
            print(i)
            for j in sizes:
                image = Image.open(f"./{path}/{i}")
                image.thumbnail((j[0], j[1]))
                image.save(f"./{destination}/{j[0]}_{i}")

        except Exception as ext:
            print(ext)



if __name__ == "__main__":
    os.makedirs("./webImages", exist_ok=True)
    resize([[300, 300], [600, 600]], sys.argv[1], "./webImages")
