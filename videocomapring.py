import cv2
from PIL import Image

import imagehash
import hashlib
import dhash

import time
import random
def hash_video(video_name):
    video = cv2.VideoCapture(video_name)
    # if not video.isOpen():
    #     print("video unable to be read")
    #     exit()
    hash_list = list()
    video_list = list()
    while True:
        ret,frame = video.read()
        if ret:
            cv2.imshow("video",frame)
            readable_hash = hashlib.md5(frame).hexdigest()
            # readable_hash = cv2.img_hash.pHash(imgg)
            print(type(readable_hash))
            print(readable_hash)
            hash_list.append(readable_hash)
            video_list.append(frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            print("end of video")
            cv2.destroyAllWindows()
            # exit()
            return hash_list, video_list

def random_frame_from_video(video_list):
    frame = random.choice(video_list)
    cv2.imshow("random image",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite("random2.png",frame)
    readable_hash = hashlib.md5(frame).hexdigest()
    return readable_hash

def compare_in_list(video_hash,image_hash):
    if image_hash in video_hash:
        print("image is part of video")

def compare_short_and_long(short_video_hash,long_video_hash):
    for i in long_video_hash:
        if i == short_video_hash[1]:
            print("got matched")
            exit()
    print("no match")

def get_image_hash():
    img = cv2.imread("random1.png")
    hash = hashlib.md5(img).hexdigest()
    return hash

print("hash long video")
long_video_hash,video_list = hash_video("fabian_numbers.mp4")
print(long_video_hash)

time.sleep(1)
print("hash short video")
short_video_hash, short_list = hash_video("fabian_numbers_Trim.mp4")
print(short_video_hash)
print(short_video_hash[1])
compare_short_and_long(short_video_hash,long_video_hash)
image_hash = get_image_hash()
compare_in_list(long_video_hash,image_hash)

# image_hash = random_frame_from_video(video_list)
#
# compare_in_set(long_video_hash,image_hash)

# print(type(image_hash))
# for i in long_video_hash:
#     if (i == image_hash):
#         print("image exist")
#     else:
#         print("bogus image")


# short_video_hash = hash_video("fabian_numbers_Trim.mp4")

# if set(short_video_hash).intersection(set(long_video_hash)):
#     print("legit video")
#
# else:
#     print("not legit video")
