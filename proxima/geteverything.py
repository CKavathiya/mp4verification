import cv2 as cv
import numpy as np


class Metrics:
    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def everything(self):
        # contrast
        contrast = 0
        brigthness = 0
        hue = 0
        sat = 0
        msg = ''
        currvar = 0


        noOfFrames = self.getNumberOfFrames()
        for i in range(0, noOfFrames):
            flag, frame = self.cap.read()

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            contrast += np.std(gray)
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            brigthness += np.mean(hsv[:, :, 2])
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            hue += + np.mean(hsv[:, :, 0])
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            sat += + np.mean(hsv[:, :, 1])
            laplacian_var = cv.Laplacian(frame, cv.CV_64F).var()
            currvar += laplacian_var

        blur = (currvar/noOfFrames)
        if (blur < 10):
            msg = 'Blur detected'
        else:
            msg = 'No blur detected'
        contrast = round((contrast/noOfFrames), 4)
        brigthness = round(brigthness / (noOfFrames), 4)
        hue = round(hue/noOfFrames, 4)
        sat = round(sat/noOfFrames, 4)

        # brightness

        return (("brigthness :", brigthness), ("contrast :", contrast), ("hue :", hue), ("saturation :", sat), ("blur detection :", msg))

    # print(everything)
