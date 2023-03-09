import cv2 as cv
import numpy as np


class Hue:
    def __init__(self, path) -> None:
        self.cap = cv.VideoCapture(path)

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getHue(self):
        hue = 0
        noOfFrames = self.getNumberOfFrames()
        for i in range(0, noOfFrames):
            flag, frame = self.cap.read()
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            hue += + np.mean(hsv[:, :, 0])

        hue = round(hue/noOfFrames, 4)
        return hue



