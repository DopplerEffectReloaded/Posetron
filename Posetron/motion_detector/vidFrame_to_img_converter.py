import cv2 as cv
import numpy as np


def vid_convert(filename, count_in):
    cap = cv.VideoCapture(filename)
    if not cap.isOpened():
        print("fail")
    count = count_in
    while True:
        retval, frame = cap.read()
        if frame is None:
            break
        cv.imwrite("C:\\Users\\SACHIN\\Body_Lang_Detection\\motion_detector\\classifying_model\\poses\\train\\shoulder\\frame%d.jpg" % count, frame)
        count += 1
    return count


if __name__ == '__main__':
    count = 0
    for i in range(6):
        count = vid_convert("C:\\Users\\SACHIN\\hand_on_shoulder\\" + str(i+1) + ".mp4", count)
