import cv2
import numpy
from datetime import time
from proxima.utils import to_secs
from proxima.frame import Frame
from proxima.proxima_exceptions import InvalidFrameException

class VideoFrameGrabber:
    def __init__(self, path: str):
        self.cap = cv2.VideoCapture(path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)


    def grabFrameAt(self, ts: time) -> Frame:
        secs = to_secs(ts)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, secs * self.fps + 1)
        _, frame = self.cap.read()
        # this is true when -O is NOT passed to the python command
        # cv2.imshow(f"debug - {ts}", frame)
        # cv2.waitKey(0)
        if frame is None:
            raise InvalidFrameException(f"No frame found at timestamp {ts}")

        return Frame(frame)


    def grabFramesBetween(self, ts1: time, ts2: time) -> Frame:
        assert(ts1 <= ts2)
        # TODO abhi: implement this later
        return []
