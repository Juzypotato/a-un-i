import cv2
import numpy as np
import speech
import time
import threading


#Global
img = "tim/idle_face.png"
words = ""


def face(): 
    print("Thread started")
    global img
    global words

    while True:
        img = "tim/idle_face.png"
        words = speech.recognize()
        if words != None:
            print(words)
            img = "tim/open_mouth.png"
            time.sleep(1)
            

            


def main():
    
    cap = cv2.VideoCapture(0)
    tim_face_thread = threading.Thread(target=face, args=(), daemon=True)
    tim_face_thread.start()
    
    while True:
        #Cam
        ret, cam = cap.read()
        
        #Tim
        tim = cv2.imread(img)
        #text = cv2.putText(tim, words, org, cv2.FONT_HERSHEY_SIMPLEX, fontScale, color, thickness, cv2.LINE_AA) 

        #Draw
        cv2.imshow('Dis you', cam)
        cv2.imshow('Tim', tim)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()