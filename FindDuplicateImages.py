from PIL import Image, ImageStat
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Combined Datasets\Testing")

duplicate_image = []

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            if file not in duplicate_image:
                path = os.path.join(root, file)
                img = Image.open(path)
                mean1 = ImageStat.Stat(img).mean

                for roots,dir,filess in os.walk(image_dir):
                    for file_check in filess:
                        if file != file_check:
                            image_check = Image.open(os.path.join(roots,file_check))
                            mean2 =ImageStat.Stat(image_check).mean

                            if mean1 == mean2:
                                duplicate_image.append(file)
                                duplicate_image.append(file_check)

print(duplicate_image)