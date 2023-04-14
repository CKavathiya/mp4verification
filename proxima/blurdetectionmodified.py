import cv2 as cv
import numpy as np

class Blur:
    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getBlur(self):
        currvar = 0
        # currframe = 0
        noOfFrames = self.getNumberOfFrames()

        for i in range(0,noOfFrames):
            ret, frame = self.cap.read()
            cv.imshow('winname',frame)
            # currframe += 1
            laplacian_var = cv.Laplacian(frame, cv.CV_64F).var()
            currvar += laplacian_var
            key = cv.waitKey(1)
            if key == 27:
                break
        blur = (currvar/noOfFrames)
        msg = ''
        if (blur < 10):
            msg = 'Blur detected'
        else:
            msg = 'No blur detected'

        self.cap.release()
        cv.destroyAllWindows()

        # cap.release()
        return msg
    
    # print(detect_blur(video_path='D:\/Pexels Videos 2609.mp4'))
