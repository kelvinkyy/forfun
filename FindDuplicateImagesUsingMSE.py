import os
import numpy as np
import cv2

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

duplicate_image = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Combined Datasets\Testing\glioma")

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path1 = os.path.join(image_dir,file)
            img1 = cv2.imread(path1)
            img1 = cv2.resize(img1, (256, 256))

            for roots,dir,filess in os.walk(image_dir):
                for file_check in filess:
                    if file != file_check:
                        path2 = os.path.join(image_dir, file_check)
                        img2 = cv2.imread(path2)
                        img2 = cv2.resize(img2, (256, 256))

                        if mse(img1,img2) <300:
                            duplicate_image.append(file)
                            duplicate_image.append(file_check)

print(duplicate_image)

