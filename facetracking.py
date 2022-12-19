import cv2, os, time, serial



faceCascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
video_capture = cv2.VideoCapture(0)

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

def arduino_write(x, y):
    arduino.write(bytes(x, 'utf-8'))
    arduino.write(bytes(y, 'utf-8'))

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5)
    
    height = frame.shape[0]
    width = frame.shape[1]

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        centerx = (2 * x + w) / 2
        centery = (2 * y + h) / 2

        scalex = centerx / width
        scaley = centery / height

        arduino_write(180 * scalex, 180 * scaley)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video_capture.release()
