from PIL import Image
import os

def resize(sizes, destination):
    try:
        os.mkdir(destination)
    except:
        print(f"{destination} folder exists!")

    for i in os.listdir("./images"):
        try:
            image = Image.open(f"./images/{i}")
            print(i)
            for j in sizes:
                image.thumbnail((j[0], j[1]))
                image.save(f"./{destination}/{j[0]}_{i}")

        except Exception as ext:
            print(ext)



if __name__ == "__main__":
    resize([[300, 300]], "./webImages")
