from __future__ import annotations
import time
import datetime
from proxima.video_analytics import VideoAnalytics
from proxima.frame import Frame
from mp4box.isofile import ISOFile
import os


class TranscodedFile:
    class MetaInfo:
        def __init__(self):
            self.size = 0
            self.playbackTime = datetime.time(0,0,0)
            self.audioFramesCount = 0
            self.videoFramesCount = 0


    def __init__(self, path: str):
        """ 
        path: path to the MP4 file
        """
        self.path = path
        self.videoAnalytics = VideoAnalytics(path)
        self.metaInfo = None


    # TODO abhi: should this be public?
    def getVideoFrameAt(self, ts: time) -> Frame: # TODO abhi: add a return type
        frame = self.videoAnalytics.grabFrameAt(ts)
        return frame


    def getMetaInfo(self):
        if self.metaInfo is None:
            isoFile = ISOFile(self.path)
            info = isoFile.get_all_info()
            self.metaInfo = TranscodedFile.MetaInfo()
            self.metaInfo.size = os.path.getsize(self.path)
            if isoFile.audio_trak is not None:
                self.metaInfo.audioFramesCount = isoFile.audio_trak.mdia.minf.stbl.stsz.sample_count
            if isoFile.video_trak is not None:
                self.metaInfo.videoFramesCount = isoFile.video_trak.mdia.minf.stbl.stsz.sample_count
            secs = info["duration"] // info["timescale"]
            self.metaInfo.playbackTime = (datetime.datetime.min + datetime.timedelta(seconds=secs)).time()

    def getAudioFrameAt(self, ts: time): # TODO abhi: add a return type
        pass


    def hasSize(self, size: int) -> TranscodedFile:
        if self.metaInfo is None:
            self.getMetaInfo()

        assert self.metaInfo.size == size
        return self


    def hasPlaybackLength(self, ts: time) -> TranscodedFile:
        if self.metaInfo is None:
            self.getMetaInfo()

        assert self.metaInfo.playbackTime == ts
        return self


    def hasVideoFrames(self, count: int) -> TranscodedFile:
        if self.metaInfo is None:
            self.getMetaInfo()

        assert self.metaInfo.videoFramesCount >= count - 50 and self.metaInfo.videoFramesCount <= count + 50
        return self


    def hasAudioFrames(self, count: int) -> TranscodedFile:
        if self.metaInfo is None:
            self.getMetaInfo()

        assert self.metaInfo.audioFramesCount >= count - 50 and self.metaInfo.audioFramesCount <= count + 50
        return self


    def hasBitrate(self, br: int) -> TranscodedFile:
        pass


    def has3x3LayoutAt(self, ts: time, n = 9) -> TranscodedFile:
        assert(self.videoAnalytics.has3x3LayoutAt(ts, n))
        return self


    def has2x2LayoutAt(self, ts: time, n = 4) -> TranscodedFile:
        assert(self.videoAnalytics.has2x2LayoutAt(ts, n))
        return self


    def has2x2LayoutBetween(self, ts1: time, ts2: time) -> TranscodedFile:
        pass


    def hasVbssLayoutAt(self, ts: time) -> TranscodedFile:
        assert(self.videoAnalytics.hasVbssLayoutAt(ts))
        return self


    def hasVbssLayoutBetween(self, ts1: time, ts2: time) -> TranscodedFile:
        pass


    def has1x2LayoutAt(self, ts: time, n = 2) -> TranscodedFile:
        assert(self.videoAnalytics.has1x2LayoutAt(ts, n))
        return self


    def has1x2LayoutBetween(self, ts1: time, ts2: time) -> TranscodedFile:
        pass


    def displaysStaticImageBetween(self, ts1: time, ts2: time) -> TranscodedFile:
        pass


    def onPane(self, id: int) -> None:
        pass


    def onPanes(self, ids: [int]) -> None:
        pass


    def goesMuteAt(self, ts: time) -> TranscodedFile:
        pass


def assertThat(file: TranscodedFile) -> TranscodedFile:
    assert(file is not None)
    return file
