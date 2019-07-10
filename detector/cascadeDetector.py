# author: Kaan Eraslan
# purpose: Detect Face on image
# usage: enter path of the model

import numpy as np
import cv2


class SimpleCascadeDetector:
    "A simple face detector"

    def __init__(self, modelPath: str,
                 imagePath: str):
        self.image = cv2.imread(imagePath)
        self.modelPath = modelPath
        self.classifier = cv2.CascadeClassifier(self.modelPath)
        self.grayimg = cv2.cvtColor(self.image.copy(), cv2.COLOR_BGR2GRAY)
        self.scaleFactor = 1.1
        self.minNeighbors = 5,
        self.minSize = (30, 30)

    def detectObjects(self):
        "Detect faces on image"
        return self.classifier.detectMultiScale(self.grayimg,
                                                scaleFactor=self.scaleFactor,
                                                minNeighbors=self.minNeighbors,
                                                minSize=self.minSize)

    def drawDetected(self, color=(0, 255, 0)):
        "Draw faces that are detected"
        drawImg = self.image.copy()
        for face in self.detectObjects():
            xcoord, ycoord, width, height = face
            cv2.rectangle(drawImg,
                          (xcoord, ycoord),
                          (xcoord+width,
                           ycoord+height),
                          color,
                          thickness=2)
        return drawImg
