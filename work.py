import cv2
import pyzbar.pyzbar as py
import pyttsx3 as pys
import pyperclip

def decode(img):
    decode = py.decode(img)
    return decode

cam = cv2.VideoCapture(0)
count = 0
time = 0
speaker = pys.init()
speaker.setProperty('rate', 145)
lst = []

while True:
    success, img = cam.read()
    x = decode(img)
    for i in x:
        data = i.data.decode('utf-8')
        lst.append(data)
        pyperclip.copy(data)
        speaker.say('copy the text successfuly')
        speaker.runAndWait()

        if data:
            count += 1
    if lst:
        cv2.putText(img, 'Press "s" to see the data ', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(img, f"type : {i.data.decode('utf-8')}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if count > 0:
        if time == 0 or time == 1:
            if key == ord('s') or key == ord('S'):
                print(data)
        else:
            pass
    if key == ord('q'):
        break