from aspect_ratio import AspectRatio
from video_length import VideoLength
from frame_rate import FrameRate
from audio_bit_rate import AudioBitRate
from video_bit_rate import VideoBitRate
from brightness import Brightness
from contrast import Contrast
from saturation import Saturation
from hue import Hue
from blurdetectionmodified import Blur
from artifactdetectionmodified import Artifact
from geteverything import Metrics
from gui import select_file


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
        self.objBlur = Blur(path)
        self.objArtifact = Artifact(path)
        self.objEverything = Metrics(path)

    def Metricstogether(self):
        self.every = self.objEverything.everything()
        self.videoLength = self.objVideoLength.getVideoLength()
        self.aspectRatio = self.objAspectRatio.getAspectRatio()
        self.frameRate = self.objFrameRate.getFrameRate()
        self.audioBitRate = self.objAudioBitRate.getAudioBitRate()
        self.videoBitRate = self.objVideoBitRate.getVideoBitRate()

    def ColorMetrics(self):
        self.brightness = self.objBrightness.getBrightness()
        self.contrast = self.objContrast.getContrast()
        self.saturation = self.objSaturation.getSaturation()
        self.hue = self.objHue.getHue()

    def BlurDetection(self):

        self.blurdetect = self.objBlur.getBlur()

    def ArtifactDetection(self):

        self.artifactdetect = self.objArtifact.getArtifact()


path = select_file()
obj = Master(path)
f = open("videoMetrics.txt", "w")


while True:
    print("------------MENU----------")
    print()
    print("1.video metrics")
    print("2.Blur detection with video")
    print("3.Object detection with video")
    print("4.EXIT")
    print()

    choice = int(input("Enter your choice :"))
    print()

    if choice == 1:
        obj.Metricstogether()
        f.write("Colour Metrics :\n")
        f.write(str(obj.every))
        f.write("\n\nOther Video Metrics :")
        f.write('\nvideoLength : ' + str(obj.videoLength))
        f.write('\naspectRatio :' + str(obj.aspectRatio))
        f.write('\nframeRate :' + str(obj.frameRate))
        f.write('\naudiobitrate :' + str(obj.audioBitRate))
        f.write('\nvideobitrate :' + str(obj.videoBitRate))
    elif choice == 2:
        obj.BlurDetection()
        f.write("\n\nBlur Detection Info:")
        f.write(str(obj.blurdetect))

    elif choice == 3:
        obj.ArtifactDetection()
        f.write("\nObject Detection Info:")
        f.write(str(obj.artifactdetect))

    elif choice == 4:
        print("Exited")
        f.close()
        break

