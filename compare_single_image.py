import cv2
import hashlib


def compare_image(image1,image2):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    hash1 = hashlib.md5(img1).hexdigest()
    hash2 = hashlib.md5(img2).hexdigest()
    print(hash1)
    print(hash2)
    if hash1 == hash2:
        print("same hash")
compare_image("random1.png","random1 - Copy.png")
