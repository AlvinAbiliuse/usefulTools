import os
import shutil
from PIL import Image

for i in os.listdir("./draw"):
    if (i.split(".")[-1] == "webp"):
            im = Image.open(f"./draw/{i}").convert("RGB")
            im.save(f"./newDraw/{i.replace('webp', '')}.jpg")
    else:
        shutil.copy(f"./draw/{i}", "./newDraw");
