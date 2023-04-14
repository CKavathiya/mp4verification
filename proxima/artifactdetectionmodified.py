import cv2 as cv
import numpy as np

class Artifact:
    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getArtifact(self):
        net = cv.dnn.readNet('D:\mp4verification-test\mp4verification-test\proxima\yolov3.weights', 'D:\mp4verification-test\mp4verification-test\proxima\yolov3.cfg')

        classes = []
        with open("D:\mp4verification-test\mp4verification-test\proxima\coco.names", "r") as f:
            classes = f.read().splitlines()

        # cap = cv2.VideoCapture('D:\opencv-4.x\opencv-4.x\samples\data/vtest.avi')
        # cap = cv2.VideoCapture('D:\/istockphoto-1199197617-640_adpp_is.mp4')
        # cap = cv.VideoCapture(video_path) #default webcam

        font = cv.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size=(100, 3))

        noOfFrames = self.getNumberOfFrames()
        for i in range(0, noOfFrames):
            _, img = self.cap.read()
            height, width, _ = img.shape

            blob = cv.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
            net.setInput(blob)
            output_layers_names = net.getUnconnectedOutLayersNames()
            layerOutputs = net.forward(output_layers_names)

            boxes = []
            confidences = []
            class_ids = []

            for output in layerOutputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.2:
                        center_x = int(detection[0]*width)
                        center_y = int(detection[1]*height)
                        w = int(detection[2]*width)
                        h = int(detection[3]*height)

                        x = int(center_x - w/2)
                        y = int(center_y - h/2)

                        boxes.append([x, y, w, h])
                        confidences.append((float(confidence)))
                        class_ids.append(class_id)

            indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)
            msg = []
            # i=0
            if len(indexes)>0:
                for i in indexes.flatten():
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    confidence = str(round(confidences[i],2))
                    color = colors[i]
                    cv.rectangle(img, (x,y), (x+w, y+h), color, 2)
                    cv.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
                    if(label != 'person'):
                        msg.append(label) 

            cv.imshow('Image', img)
            key = cv.waitKey(1)
            if key==27:
                break
        self.cap.release()
        cv.destroyAllWindows()
        res = [*set(msg)]      
        return ('Objects detected :',res)

    # print(getArtifact("D:\/istockphoto-1199197617-640_adpp_is.mp4"))