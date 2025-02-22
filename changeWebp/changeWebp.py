import os
import shutil
from PIL import Image
import sys

arg = sys.argv[1]

for i in os.listdir(arg):
    os.makedirs(f"./copy/{arg}", exist_ok=True)
    print(i)
    if (i.split(".")[-1] == "webp"):
            im = Image.open(f"./{arg}/{i}").convert("RGB")
            im.save(f"./copy/{arg}/{i.replace('webp', '')}jpg")
    else:
        shutil.copy(f"./{arg}/{i}", f"./copy/{arg}");
