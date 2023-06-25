import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture('video_test.mp4')

while True:
    _, frame = cap.read()  
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break