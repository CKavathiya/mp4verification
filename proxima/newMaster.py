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
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import threading
import customtkinter as ctk
import os
from handdetection import hdetection
class Master:
    def __init__(self) -> None:
        pass

    def intialize(self, path) -> None:
        self.path = path
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
        self.objHand=hdetection(path)

    def Metricstogether(self):
        self.every = self.objEverything.everything()
        self.videoLength = self.objVideoLength.getVideoLength()
        self.aspectRatio = self.objAspectRatio.getAspectRatio()
        self.frameRate = self.objFrameRate.getFrameRate()
        self.audioBitRate = self.objAudioBitRate.getAudioBitRate()
        self.videoBitRate = self.objVideoBitRate.getVideoBitRate()

    def BlurDetection(self):
        self.blurdetect = self.objBlur.getBlur()

    def ArtifactDetection(self):
        self.artifactdetect = self.objArtifact.getArtifact()
    def HandDetection(self):
        self.handdetect=self.objHand.detect()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Video Metrics")
root.iconbitmap(os.path.join("Files","icon.ico"))
root.geometry("1030x505")
root.resizable(0, 0)
my_font = tk.font.Font(size=12, weight="bold")

left_frame = ctk.CTkFrame(root, corner_radius=15)
left_frame.grid(row=0, column=0, sticky="ns", padx=5, pady=10)
left_frame.columnconfigure(0, weight=1)
right_frame = ctk.CTkFrame(root, corner_radius=15)
right_frame.grid(row=0, column=2, sticky="nswe", padx=5, pady=10)

text = Text(left_frame, height=30, width=105, wrap=WORD,bd=0, bg="#212121", fg="silver", font=my_font)
text.tag_config("green", background="green", foreground="silver")
text.grid(row=0, column=0, padx=15, pady=15)


def writeIntoTextArea(text, color=None):
    text_widget = left_frame.winfo_children()[0]
    text_widget.insert(tk.END, text+"\n", color)


def selectFile(obj):
    text.delete("1.0", "end")
    file_path = filedialog.askopenfilename(filetypes=[('MP4 files', '*.mp4')])
    obj.path = file_path
    obj.intialize(file_path)
    disableBtn(btn1)
    enableBtn(btn2)
    enableBtn(btn3)

def btn2_func(obj):
    disableBtn(btn1)
    obj.Metricstogether()

    writeIntoTextArea('videoLength : ' + str(obj.videoLength)+" seconds")
    writeIntoTextArea('\naspectRatio :' + str(obj.aspectRatio))
    writeIntoTextArea('\nframeRate :' + str(obj.frameRate) + " fps")

    if obj.audioBitRate != None:
        writeIntoTextArea('\naudiobitrate :' + str(obj.audioBitRate) + " bps")
    else:
        writeIntoTextArea('\naudiobitrate :' "No Audio Detected")

    if obj.videoBitRate != None:
        writeIntoTextArea('\nvideobitrate :' + str(obj.videoBitRate) + " bps")
    else:
        writeIntoTextArea('\nvideobitrate :' "No Video Detected")

    writeIntoTextArea('\nBrightness : ' + str(obj.every[0])+" (0-255)")
    writeIntoTextArea('\nContrast : ' + str(obj.every[1])+" (0-255)")
    writeIntoTextArea('\nHue : ' + str(obj.every[2])+" (0-255)")
    writeIntoTextArea('\nSaturation : ' + str(obj.every[3])+" (0-255)")
    writeIntoTextArea('\nBlurr Detection Information : ' + str(obj.every[4]))
    disableBtn(btn2)
    


def btn3_func(obj):
    obj.ArtifactDetection()
    writeIntoTextArea("\nObject Detection Info:")
    writeIntoTextArea(str(obj.artifactdetect))
    disableBtn(btn3)
    enableBtn(btn5)

def btn5_func(obj):
    obj.HandDetection()
    writeIntoTextArea("\nGesture Detection Info:")
    writeIntoTextArea(str(obj.handdetect))
    disableBtn(btn5)
    enableBtn(btn4)

def findFileName(obj):
    tuples = obj.path.split('/')
    fileNameWithExt = tuples[len(tuples)-1]
    fileName = fileNameWithExt[0:len(fileNameWithExt)-4]
    fileName += ".txt"
    return fileName

def btn4_func(obj):
    fileName = findFileName(obj)
    f = open(fileName, "w")
    f.write('videoLength : ' + str(obj.videoLength)+" seconds")
    f.write('\naspectRatio :' + str(obj.aspectRatio))
    f.write('\nframeRate :' + str(obj.frameRate)+" fps")
    f.write('\naudiobitrate :' + str(obj.audioBitRate)+" bps")
    f.write('\nvideobitrate :' + str(obj.videoBitRate)+" bps")
    f.write('\nBrightness : ' + str(obj.every[0])+" (0-255)")
    f.write('\nContrast : ' + str(obj.every[1])+" (0-255)")
    f.write('\nHue : ' + str(obj.every[2])+" (0-255)")
    f.write('\nSaturation : ' + str(obj.every[3])+" (0-255)")
    f.write('\n\nBlurr Detection Information : ' + str(obj.every[4]))
    f.write("\nObject Detection Info:")
    f.write(str(obj.artifactdetect))
    f.write("\nGesture Detection Info:")
    f.write(str(obj.handdetect))
    writeIntoTextArea("\n")
    writeIntoTextArea("Text File Ready", "green")
    f.close()
    disableAllButtons()
    enableBtn(btn1)
    enableBtn(btn6)
    
    


obj = Master()

btn1 = ctk.CTkButton(right_frame, text=" Select File ",command=lambda: selectFile(obj), corner_radius=18)
btn1.grid(sticky="ew", row=0, column=0, padx=25, pady=15, ipadx=20)

btn2 = ctk.CTkButton(right_frame, text=" Video Metrics       ", command=lambda: threading.Thread(target=btn2_func, args=(obj,)).start(), corner_radius=18)
btn2.grid(sticky="ew", row=1, column=0, padx=25, pady=15, ipadx=15)

btn3 = ctk.CTkButton(right_frame, text=" Object Detection    ",command=lambda: btn3_func(obj), corner_radius=18)
btn3.grid(sticky="ew", row=3, column=0, padx=25, pady=15, ipadx=20)

btn5 = ctk.CTkButton(right_frame, text=" Gesture Detection",command=lambda: btn5_func(obj), corner_radius=18)
btn5.grid(sticky="ew", row=4, column=0, padx=25, pady=15, ipadx=20)

btn4 = ctk.CTkButton(right_frame, text=" Write Output to File",command=lambda: btn4_func(obj), corner_radius=18)
btn4.grid(sticky="ew", row=5, column=0, padx=25, pady=15, ipadx=20)

btn6 = ctk.CTkButton(right_frame, text=" Exit ",command=root.destroy, corner_radius=18)
btn6.grid(sticky="ew", row=6, column=0, padx=25, pady=15, ipadx=20)


def disableAllButtons():
    btn2.configure(state="disabled")
    btn3.configure(state="disabled")
    btn4.configure(state="disabled")
    btn5.configure(state="disabled")


def disableBtn(btn):
    btn.configure(state="disabled")

def enableBtn(btn):
    btn.configure(state="normal")



disableAllButtons()
root.mainloop()
