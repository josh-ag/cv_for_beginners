import cv2 as cv

# read video from camera feed
camera = cv.VideoCapture(0)
# read from vid_file
# video = cv.VideoCapture('videos/ai.mp4')


# rescale frame (live/offline video)
def rescale_frame(frame,scale=2):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# resize video frame (live feeds only) 
def resize_frame(width=400,height=400,brightness=30):
    camera.set(cv.CAP_PROP_FRAME_WIDTH,width)
    camera.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    camera.set(cv.CAP_PROP_BRIGHTNESS,brightness)

# resize_frame()

# if not camera.isOpened():
#     print('Cannot open camera')
#     exit()

# write/save video
# 1. Define codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('videos/flipped.avi', fourcc,30.0,(640,480))

# read vid frame-by-frame 
while camera.isOpened():
    isTrue,frame = camera.read()

    if not isTrue:
        print("Can't recieve frame (stream end?). Exiting ...")
        break

    # read as grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    rescaled = rescale_frame(frame)
    out.write(cv.flip(frame,0))

    # display vid 
    cv.imshow('Grayed Video', gray)
    cv.imshow('Rescaled Video', rescaled)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break



# # write/save video
# # 1. Define codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('videos/Camera.avi', fourcc,20.0,(640,480))

# read video frame_by_frame
# while True:
#     ret, frame = camera.read()
#     if not ret:
#         print("Can't recieve frame (stream ended?). Exiting...")
#         break

#     # frame = cv.flip(frame,0)

#     # write the flipped frame
#     out.write(frame)

#     cv.imshow('Frame', frame)
#     if cv.waitKey(0) & 0XFF == ord('d'):
#         break


#CAMERA SPECIFIC CONSTANT
# GETS camera width
print(f'CAMERA WIDTH: {camera.get(cv.CAP_PROP_FRAME_WIDTH)}')
# GETS camera height
print(f'CAMERA HEIGHT: {camera.get(cv.CAP_PROP_FRAME_HEIGHT)}')
# GETS camera frame count
print(f'CAMERA FRAME COUNT: {camera.get(cv.CAP_PROP_FRAME_COUNT)}')
# GETS camera frame count
print(f'CAMERA FORMAT: {camera.get(cv.CAP_PROP_FORMAT)}')

# When everything done, release the capture
camera.release()
cv.destroyAllWindows()