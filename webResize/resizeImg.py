from PIL import Image
import os

def resize(sizes, destination):
    try:
        os.mkdir("./resizedImages")
    except:
        print("resizedImages folder exists!")

    for i in os.listdir("./images"):
        try:
            image = Image.open(f"./images/{i}")
            print(i)
            image.thumbnail((300, 300))
            image.save(f"./resizedImages/resized_{i}")

        except Exception:
            print(Exception)




