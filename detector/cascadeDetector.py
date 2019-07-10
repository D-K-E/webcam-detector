# author: Kaan Eraslan
# purpose: Detect Face on image
# usage: enter path of the model

import numpy as np
import cv2
import os


class SimpleCascadeDetector:
    "A simple face detector"

    def __init__(self, modelPath: str,
                 imagePath: str):
        if imagePath is not None:
            self.image = cv2.imread(imagePath)
            self.grayimg = cv2.cvtColor(self.image.copy(), cv2.COLOR_BGR2GRAY)
        else:
            self.image = None
            self.grayimg = None
        self.modelPath = modelPath

        self.scaleFactor = 1.1
        self.minNeighbors = 5
        self.minSize = (30, 30)

    def detectObjects(self):
        "Detect faces on image"
        print(self.modelPath)
        self.classifier = cv2.CascadeClassifier()
        retval = self.classifier.load(self.modelPath)
        if not retval:
            print(self.modelPath)
            if os.path.isfile(self.modelPath):
                print('file exists')
            else:
                print('file not exist')
        objects = self.classifier.detectMultiScale(self.grayimg,
                                                   self.scaleFactor,
                                                   self.minNeighbors,
                                                   )

        return objects

    def drawDetected(self, color=(0, 255, 0)):
        "Draw faces that are detected"
        drawImg = self.image.copy()
        objects = self.detectObjects()
        for obj in objects:
            xcoord, ycoord, width, height = obj
            cv2.rectangle(drawImg,
                          (xcoord, ycoord),
                          (xcoord+width,
                           ycoord+height),
                          color,
                          thickness=2)
        return drawImg

    def setImage(self, img: np.ndarray) -> None:
        "Set image to classifier"
        assert img.dtype == 'uint8'
        imcopy = img.copy()
        self.image = imcopy
        self.grayimg = cv2.cvtColor(imcopy, cv2.COLOR_BGR2GRAY)
        return
