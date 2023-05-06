# @desc - READ VIDEO FILE
import cv2 as cv

# read image
video = cv.VideoCapture('videos/ai.mp4')

def rescaleFrame(frame,scale=1.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# @desc - read video frames
while True:
    _,frame = video.read()

    resize_frame = rescaleFrame(frame)

    cv.imshow('Cv Video', frame)
    cv.imshow('Cv Resized_Video', resize_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# await keypress to close window
video.release()
cv.destroyAllWindows()