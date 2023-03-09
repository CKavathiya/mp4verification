from proxima.video_grab import VideoFrameGrabber
from datetime import time

class VideoAnalytics:
    def __init__(self, path):
        self.frameGrabber = VideoFrameGrabber(path)
        self.framesCache = {} # memoize frames and panes in them


    def grabFrameAt(self, ts: time):
        if ts in self.framesCache:
            return self.framesCache[ts]

        frame = self.frameGrabber.grabFrameAt(ts)
        self.framesCache[ts] = frame
        return frame


    def has3x3LayoutAt(self, ts: time, n = 9):
        frame = self.grabFrameAt(ts)
        return frame.has3x3Layout(n)


    def has2x2LayoutAt(self, ts: time, n = 4):
        frame = self.grabFrameAt(ts)
        return frame.has2x2Layout(n)


    def has1x2LayoutAt(self, ts: time, n = 2):
        frame = self.grabFrameAt(ts)
        return frame.has1x2Layout(n)


    def hasVbssLayoutAt(self, ts: time):
        frame = self.grabFrameAt(ts)
        return frame.hasVBSSLayout()
