import cv2 as cv
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

        # Load the gesture recognizer model
model = load_model("D:\mp4verification-testpy\proxima\mp_hand_gesture")

        # Load class names
f = open("D:\mp4verification-testpy\proxima\gesture.names", 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)
        # noOfFrames = self.getNumberOfFrames()

class hdetection:
    def __init__(self, path) -> None:
        self.path = path
        self.cap = cv.VideoCapture(self.path)

    def getNumberOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def detect(self):
        

        noOfFrames = self.getNumberOfFrames()
        # className=''
        
        msg = set()
        for i in range(0, noOfFrames):
        # Read each frame from the webcam
            _, img = self.cap.read()

            x, y, c = img.shape

            # Flip the frame vertically
            img = cv.flip(img, 1)
            framergb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

            # Get hand landmark prediction
            result = hands.process(framergb)

            # print(result)
            
            className = ''

            # post process the result
            if result.multi_hand_landmarks:
                landmarks = []
                for handslms in result.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        # print(id, lm)
                        lmx = int(lm.x * x)
                        lmy = int(lm.y * y)

                        landmarks.append([lmx, lmy])

                    # Drawing landmarks on frames
                    mpDraw.draw_landmarks(img, handslms, mpHands.HAND_CONNECTIONS)

                    # Predict gesture
                    prediction = model.predict([landmarks])
                    # print(prediction)
                    classID = np.argmax(prediction)
                    className = classNames[classID]

            # show the prediction on the frame
            cv.putText(img, className, (10, 50), cv.FONT_HERSHEY_SIMPLEX, 
                        1, (0,0,255), 2, cv.LINE_AA)
            msg.add(className)   
          
            # Show the final output
            cv.imshow("Output", img) 

            if cv.waitKey(1) == ord('q'):
                break

        # release the webcam and destroy all active windows
        self.cap.release()

        cv.destroyAllWindows()
        # res = [*set(msg)]      
        return msg

    
    