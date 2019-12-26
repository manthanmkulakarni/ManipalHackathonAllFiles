from __future__ import print_function
import cv2 as cv
import argparse
from PIL import Image
import numpy as np

def detectAndDisplay(frame):
    font = cv.FONT_HERSHEY_SIMPLEX
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray=cv.GaussianBlur(frame_gray, (5,5),3) 
    frame_gray = cv.equalizeHist(frame_gray)
    
    #-- Detect faces
    eye_center=0
    radius=0
    faces = face_cascade.detectMultiScale(frame_gray)
    
  

    

    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 5)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
     
        
       

      
        

         
        

    
           

    return frame
    
    
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascades/cascade.xml')



parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade



face_cascade = cv.CascadeClassifier()





#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
   




camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

camera = cv.VideoCapture(0)
image=0
while True:
    return_value,image = camera.read()
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    detectAndDisplay(image)
    
    #cv.putText(image, 'face', (image.shape[0]/2,image.shape[1]/2), font, 3, (0, 255, 0), 2, cv.LINE_AA)
    cv.imshow('image',image)
    if cv.waitKey(1)& 0xFF == ord('s'):
        cv.imwrite('test.jpg',image)
        break
camera.release()
cv.destroyAllWindows()
    
#detectAndDisplay(image)

    
