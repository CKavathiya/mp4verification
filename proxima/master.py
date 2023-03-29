from aspect_ratio import AspectRatio
from video_length import VideoLength
from frame_rate import FrameRate
from audio_bit_rate import AudioBitRate
from video_bit_rate import VideoBitRate
from brightness import Brightness
from contrast import Contrast
from saturation import Saturation
from hue import Hue
from gui import select_file



class Master:
    def __init__(self, path) -> None:
        print("Writing into the file....")
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
        f = open("videoMetrics.txt", "w")
        f.write("Video Length:"+ str(self.videoLength))
        f.write("\nVideo Aspect Ration:"+ str(self.aspectRatio))
        f.write("\nVideo frameRate:"+ str(self.frameRate))
        f.write("\nVideo audioBitRate:"+ str(self.audioBitRate))
        f.write("\nVideo videoBitRate:"+ str(self.videoBitRate))
        f.write("\nVideo brightness:"+ str(self.brightness))
        f.write("\nVideo contrast:"+ str(self.contrast))
        f.write("\nVideo saturation:"+ str(self.saturation))
        f.write("\nVideo hue:"+ str(self.hue))
        f.close()
        print("Done Writing into file")

path=select_file()
obj = Master(path)
obj.getDetails()





