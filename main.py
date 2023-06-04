import cv2

# load the cascade data from file provided by opencv 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# load facecam
cam = cv2.VideoCapture(2)

while (True):

    # ret is the return from .read() but since the cam is continuous, we won't need it.
    ret, frame = cam.read()

    # set up the detection for faces using the facecam frame
    faces = face_cascade.detectMultiScale(
        frame,
        # use minNeighbors to minimize potential false positives of faces. The higher the number, the more cv2 looks for repeated squares from frame to frame to classify faces.
        minNeighbors=5,
        # minimum size to detect in px
        minSize=(20,20),
    )
    # eyes = eye_cascade.detectMultiScale(
    #     frame,
    #     minNeighbors=5,
    #     minSize=(20,20),
    # )
    # smile = smile_cascade.detectMultiScale(
    #     frame,
    #     minNeighbors=5,
    #     minSize=(20,20),
    # )

    # draw the rectangle over the faces on frame starting at x,y and ending at x+w, y+h. Has BGR color and thickness at the end
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    # for (x,y,w,h) in eyes:
    #     cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    # for (x,y,w,h) in smile:
    #     cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    
    # show frame
    cv2.imshow('frame', frame)

    # waits for esc key to be pressed to stop processes.
    if cv2.waitKey(1) == (27):
        cam.release()
        cv2.destroyAllWindows()
        break

