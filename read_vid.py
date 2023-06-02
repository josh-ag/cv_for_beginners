import cv2 as cv

# read video from camera feed
camera = cv.VideoCapture(0)
# read from vid_file
video = cv.VideoCapture('videos/ai.mp4')

# resize frame (for live feeds only) 
# def resize_frame(width=400,height=400,brightness=200):
#     camera.set(3,width)
#     camera.set(4, height)
#     camera.set(10,brightness)

# rescale frame
def rescale_frame(frame,scale=1.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# @desc - read through video frames
while True:
    # _,frame = video.read()
    isTrue, frame = camera.read()

    resized = rescale_frame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# await keypress to close window
camera.release()
cv.destroyAllWindows()