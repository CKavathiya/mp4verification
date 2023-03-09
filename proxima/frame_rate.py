import cv2 as cv


class FrameRate:
    def __init__(self,path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getFrameRate(self):
        return int((self.cap).get(cv.CAP_PROP_FPS))



