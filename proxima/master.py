from aspect_ratio import AspectRatio
from video_length import VideoLength
from frame_rate import FrameRate
from audio_bit_rate import AudioBitRate
from video_bit_rate import VideoBitRate
from brightness import Brightness
from contrast import Contrast
from saturation import Saturation
from hue import Hue


class Master:
    def __init__(self, path) -> None:

        self.objVideoLength = VideoLength(path)
        self.objAspectRatio = AspectRatio(path)
        self.objFrameRate = FrameRate(path)
        self.objAudioBitRate = AudioBitRate(path)
        self.objVideoBitRate = VideoBitRate(path)
        self.objBrightness = Brightness(path)
        self.objContrast = Contrast(path)
        self.objSaturation = Saturation(path)
        self.objHue = Hue(path)

    def getDetails(self):
        self.videoLength=self.objVideoLength.getVideoLength()
        self.aspectRatio=self.objAspectRatio.getAspectRatio()
        self.frameRate=self.objFrameRate.getFrameRate()
        self.audioBitRate=self.objAudioBitRate.getAudioBitRate()
        self.videoBitRate=self.objVideoBitRate.getVideoBitRate()
        self.brightness=self.objBrightness.getBrightness()
        self.contrast=self.objContrast.getContrast()
        self.saturation=self.objSaturation.getSaturation()
        self.hue=self.objHue.getHue()

        


obj = Master(r"E:\HMS\Coding\Media\darkVid.mp4")

obj.getDetails()

print(obj.videoLength)
print(obj.aspectRatio)
print(obj.frameRate)
print(obj.audioBitRate)
print(obj.videoBitRate)
print(obj.brightness)
print(obj.contrast)
print(obj.saturation)
print(obj.hue)



