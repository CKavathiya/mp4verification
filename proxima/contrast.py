import cv2 as cv
import numpy as np

class Contrast:
    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getContrast(self):
        contrast=0
        noOfFrames = self.getNumberOfFrames()
        for i in range(0, noOfFrames):
            flag, frame = self.cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            contrast += np.std(gray)

        contrast = round((contrast/noOfFrames), 4)
        return contrast


