# author: Kaan Eraslan
# purpose: Detect objects using webcam
# usage: enter path of the model

import numpy as np
import tensorflow as tf
import cv2
import os
import sys
from cascadeDetector import SimpleCascadeDetector


def drawRect(xcoord: int, ycoord: int,
             width: int, height: int,
             img: np.ndarray,
             color=(0, 255, 0),
             thickness=2):
    "Draw rectangle using x, y coordinate"
    assert img.dtype == 'uint8'
    imcopy = img.copy()
    return cv2.rectangle(imcopy,
                         (xcoord, ycoord),
                         (xcoord+width,
                          ycoord+height),
                         color, thickness)


if __name__ == '__main__':
    print("Welcome to simple webcam detector")
    print("The purpose of this program is to detect objects using your webcam")
    print("You can detect the objects of the following type: ")
    print("  - Face (f)")
    print("  - Noise (n)")
    print("  - Eyes (e)")
    print("  - Facial Key Points (k)")
    print("Choose your feature by writting")
