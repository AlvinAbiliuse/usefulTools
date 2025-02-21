import os
import shutil
from PIL import Image
import sys

arg = sys.argv[1]

for i in os.listdir(arg):
    os.makedirs(f"./{arg}-copy", exist_ok=True)
    if (i.split(".")[-1] == "webp"):
            im = Image.open(f"./{arg}/{i}").convert("RGB")
            im.save(f"./{arg}-copy/{i.replace('webp', '')}.jpg")
    else:
        shutil.copy(f"./{arg}/{i}", f"./{arg}-copy");
