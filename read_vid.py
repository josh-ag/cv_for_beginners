
import cv2 as cv

# read video
# camera feed 
camera_vid = cv.VideoCapture(0)
# from path 
video = cv.VideoCapture('videos/ai.mp4')

# resize frame (for live feeds only) 
def resize_frame(width=1200,height=720,brightness=20):
    camera_vid.set(3,width)
    camera_vid.set(4, height)
    camera_vid.set(10,brightness)



# rescale frame
def rescale_frame(frame,scale=1.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# @desc - read through video frames
while True:
    _,frame = video.read()
    isTrue, frame = camera_vid.read()

    # resize_frame = rescale_frame(frame)
    cv.imshow('Default Video', frame)
    # cv.imshow('Resized Video', resize_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# await keypress to close window
camera_vid.release()
cv.destroyAllWindows()