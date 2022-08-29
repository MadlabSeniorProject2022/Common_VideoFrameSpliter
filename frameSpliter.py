import cv2
import numpy as np
import os


def framecapture(source: cv2.Mat, path: str, name: str = "frame"):
    if not os.path.exists(path):
        os.mkdir(path)
    frameNum = 0
    while (True):
        success, frame = source.read()
        if success:
            cv2.imwrite(f'{path}{name}{frameNum}.jpg', frame)
        else:
            break
        frameNum = frameNum+1

    source.release()
