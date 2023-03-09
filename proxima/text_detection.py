import pytesseract
import cv2
import os


class TextDetection:
    pytesseract.pytesseract.tesseract_cmd = os.environ["TESSERACT_EXE_PATH"]

    @staticmethod
    def getTextOn(pane) -> str:
        # cv2.imshow("test", pane)
        # cv2.waitKey(0)
        text = pytesseract.image_to_string(pane)
        return text