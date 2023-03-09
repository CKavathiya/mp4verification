from proxima.text_detection import TextDetection
import cv2


class Pane:
    def __init__(self, img):
        self.__img = img


    def hasText(self, text: str) -> bool:
        res = self.__img
        h, w, _ = res.shape
        if w < 960: # zoom only when we have a small pane (one shown in the bottom bar)
            res = cv2.resize(res, None, fx=2, fy=2)

        # cv2.imshow(f"debug {h}x{w}", res)
        # cv2.waitKey(0)
        detected_text = TextDetection.getTextOn(res)
        assert detected_text == text
        return True

