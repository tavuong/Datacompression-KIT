import numpy as np
import cv2
from lib.codec_dct import *
import config

def camera_CODEC (param=0):
    cap = cv2.VideoCapture(0)


# Define the codec and create VideoWriter object
# RPI einstelllung
#  fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  

# 160 x 120
# 320 x 240
# 640 x 480 (480p)
# 1280 x 720 (720p)
# 1920 x 1080 (1080p; make sure your camera supports this high resolution.)


    out = cv2.VideoWriter(config.dirImgout + '/livecam.mp4',fourcc, 15.0, (640,480))    
#    fourcc = cv2.VideoWriter_fourcc(*'XVID')
#    out = cv2.VideoWriter('./img_out/output.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
#           frame = cv2.flip(frame,0)
#            frame = coder(frame,400)

#           write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
#            if cv2.waitKey(1) & 0xFF == ord('q'):
            if cv2.waitKey(33) == 27:
                break
        else:
            break

# Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return(True)

def image_Click (param=0):
    CAMERA_DEVICE_ID = 0
    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 480
    
    # create video capture
    cap = cv2.VideoCapture(CAMERA_DEVICE_ID)

    # set resolution to 320x240 to reduce latency 
    cap.set(3, IMAGE_WIDTH)
    cap.set(4, IMAGE_HEIGHT)

    # Loop to continuously get images
    while True:
        # Read the frames from a camera
        _, frame = cap.read()
        
        # show image
        cv2.imshow('frame', frame)
        
        # if key pressed is 'Esc' then exit the loop
        if cv2.waitKey(33) == 27:
            cv2.imwrite(config.dirImgout + '/capture.jpg',frame)
            break
    # Clean up and exit the program
    cv2.destroyAllWindows()
    cap.release()
    return(True)
