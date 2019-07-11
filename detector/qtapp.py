# author: Kaan Eraslan
# purpose: Detect objects using webcam
# usage: enter path of the model

import numpy as np
import cv2
import os
import sys
from PySide2 import QtGui, QtCore, QtWidgets
from detector.cascadeDetector import SimpleCascadeDetector
from PIL import Image
from detector.assets.ui.interface import Ui_MainWindow
import datetime


class AppWindowInit(Ui_MainWindow):
    """
    Initializes the image window
    made in qt designer
    """

    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        super().setupUi(self.main_window)
        pass


class AppWindowFinal(AppWindowInit):
    "Final application window"

    def __init__(self):
        super().__init__()
        self.videoSize = self.graphicsView.size()
        self.videoCapture = None

        # Main Window Events
        self.main_window.setWindowTitle("A Simple Detector using Webcam")
        self.main_window.closeEvent = self.closeApp

        curdir = os.curdir
        curdir = os.path.abspath(curdir)
        detectorDir = os.path.join(curdir, 'detector')
        self.assetsdir = os.path.join(detectorDir, 'assets')
        modelsDir = os.path.join(self.assetsdir, 'models')

        # object types
        self.objTypes = {
            'faceParts': {
                "Eye": os.path.join(modelsDir, 'cascadeEye.xml'),
                "Right Eye": os.path.join(modelsDir, 'cascadeRightEye.xml'),
                "Left Eye": os.path.join(modelsDir, 'cascadeLeftEye.xml'),
                "Human Smile": os.path.join(modelsDir,
                                        'cascadeSmile.xml'),
            },
            # "Nose": os.path.join(modelsDir, 'cascadeEye.xml'),
            "Frontal Cat Face": os.path.join(modelsDir,
                                             'cascadeFrontalCatFace.xml'),
            "Frontal Human Face": os.path.join(modelsDir,
                                               'cascadeFrontalFace.xml'),
            "Profile Human Face": os.path.join(modelsDir,
                                               'cascadeProfileFace.xml'),
            
            "Frontal Facial Key Points": "",
        }
        self.facePart = self.objTypes['faceParts']
        self.modelPath = {}
        for key, val in self.objTypes.items():
            if key == "faceParts":
                for k, v in self.facePart.items():
                    self.modelPath[k] = v
            else:
                self.modelPath[key] = val
        self.cascadeClassifiers = [
            k for k, v in self.modelPath.items() if 'cascade' in v
        ]
        self.kerasClassifiers = [
            k for k, v in self.modelPath.items() if 'keras' in v
        ]
        combovals = list(self.modelPath.keys())
        self.objectTypes.addItems(combovals)
        self.scene = QtWidgets.QGraphicsScene()
        self.frame = None

        # shortcuts
        self.closeShortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("ctrl+w"), self.centralwidget
        )
        self.startShortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("ctrl+a"), self.centralwidget
        )
        self.stopShortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("ctrl+e"), self.centralwidget
        )
        self.captureShortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("ctrl+f"), self.centralwidget
        )

        # buttons
        self.startFeedBtn.clicked.connect(self.startFeed)
        self.stopFeedBtn.clicked.connect(self.stopFeed)
        self.captureImageBtn.clicked.connect(self.saveCapture)
        self.objectTypes.currentTextChanged.connect(
            self.restartFeed)

        # shortcut wiring
        self.closeShortcut.activated.connect(self.quickClose)
        self.startShortcut.activated.connect(self.startFeed)
        self.stopShortcut.activated.connect(self.stopFeed)
        self.captureShortcut.activated.connect(self.saveCapture)

    def restartFeed(self):
        "Restart the feed"
        if self.videoCapture is not None:
            self.videoCapture.release()
            self.startFeed()

    def startFeed(self):
        "start webcam feed and classifying"
        self.videoCapture = cv2.VideoCapture(0)  # assuming single camera
        self.videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH,
                              self.videoSize.width())
        self.videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,
                              self.videoSize.height())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.displayImage)
        self.timer.start(30)

    def stopFeed(self):
        "Stop webcam feed"
        self.timer.stop()
        self.scene.clear()
        self.videoCapture.release()

    def chooseClassifier(self, choice: str):
        "Instantiate a classifier based on choice"
        if choice in self.cascadeClassifiers:
            modelPath = self.modelPath[choice]
            classifier = SimpleCascadeDetector(modelPath,
                                               imagePath=None)
        elif choice in self.kerasClassifiers:
            classifer = None
        return classifier

    def detectFaceInFrame(self, frame: np.ndarray):
        "Detect face in frame and output detected faces"
        choice = "Frontal Human Face"
        classifier = self.chooseClassifier(choice)
        classifier.setImage(frame.copy())
        return classifier.detectObjects()

    def detectObjectInFrame(self, frame: np.ndarray):
        "Detect object in frame"
        choice = self.objectTypes.currentText()
        if choice in self.facePart:
            classifier = self.chooseClassifier(choice)
            faces = self.detectFaceInFrame(frame)
            image = frame.copy()
            for face in faces:
                xcoord, ycoord, width, height = face
                faceImg = image[ycoord:ycoord+height,
                                xcoord:xcoord+width]
                classifier.setImage(faceImg)
                detectedImg = classifier.drawDetected()
                image[ycoord:ycoord+height,
                      xcoord:xcoord+width] = detectedImg
            return image
        else:
            classifier = self.chooseClassifier(choice)
            classifier.setImage(frame)
            return classifier.drawDetected()

    def displayImage(self):
        "Display the frame image on scene after detection"
        self.scene.clear()
        gw, gh = self.graphicsView.width(), self.graphicsView.height()
        capt, self.frame = self.videoCapture.read()
        self.frame = self.detectObjectInFrame(self.frame)
        frame = self.frame.copy()
        frame = cv2.resize(frame, dsize=(gw, gh), 
                           interpolation=cv2.INTER_LINEAR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        qimage = QtGui.QImage(frame,
                              frame.shape[1],  # width/columns
                              frame.shape[0],  # height/rows
                              frame.strides[0],
                              QtGui.QImage.Format_RGB888)
        qpixmap = QtGui.QPixmap.fromImage(qimage)
        self.scene.setSceneRect(0, 0, gw, gh)
        self.scene.addPixmap(qpixmap)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

    def saveCapture(self):
        "Save capture to file"
        path = os.path.join(self.assetsdir, "output")
        todayStr = str(datetime.date.today())
        saveName = os.path.join(path, "capture-" + todayStr + ".png")
        #
        cv2.imwrite(saveName, self.frame)

    def showInterface(self):
        "Show the interface"
        self.main_window.show()

    # Standard gui
    def closeApp(self, event):
        "Close application"
        reply = QtWidgets.QMessageBox.question(
            self.centralwidget, 'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()
            #
        return

    def quickClose(self):
        "Quick close"
        sys.exit(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AppWindowFinal()
    window.showInterface()
    sys.exit(app.exec_())
