import cv2
import mediapipe as mp
import time
from mss import mss
from PIL import Image
import numpy as np
import keyboard
import mouse

# face detection

mpFaceDetection = mp.solutions.face_detection

faceDetection = mpFaceDetection.FaceDetection()

cTime = cTime = time.time()
pTime = cTime

mon = {'left': 0, 'top': 0, 'width': 1920, 'height': 1080}

recording = False
detected = False
timeout = 180
refreshTime = 300

with mss() as sct:
    while True:
        cTime = time.time()
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB',
            (screenShot.width, screenShot.height),
            screenShot.rgb,
        )
        img2 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        imgRGB = np.array(img)
        #detect face in image
        results = faceDetection.process(imgRGB)
        if results.detections:
            # if detected
            pTime = cTime
            if not detected:
                detected = True
                print("\nDetected")

            if not recording :
                keyboard.press_and_release("f5")
                time.sleep(3)
                mouse.move(300, 500)
                time.sleep(3)
                mouse.double_click("left")

                keyboard.press_and_release("ctrl + f1")
                recording = True
                print("Begin Recording")
            else:
                time.sleep(1)
                continue


            # # detection metadata
            # print("detected\n")
            # print("faces detected: " +str(len(results.detections)))
            # for id, detection in enumerate(results.detections):
            #     print(detection.score[0])

            # # print bounding box
            # for id, detection in enumerate(results.detections):
            #     bboxC = detection.location_data.relative_bounding_box
            #     ih, iw, ic = img2.shape
            #     bbox = int(bboxC.xmin* iw), int(bboxC.ymin * ih), \
            #             int(bboxC.width * iw), int(bboxC.height * ih)
            #     cv2.rectangle(img2, bbox, (255, 0, 255), 2)
        else:
            if detected:
                print("\nLost detection")
                detected = False
            if recording:
                timePassed = cTime - pTime
                print("Timeout in :" + str(timeout - int(timePassed)))

                if timePassed > timeout:
                    keyboard.press_and_release("ctrl + f2")
                    recording = False
                    print("End Recording\n")
                    pTime = cTime
                else:
                    time.sleep(1)
                    continue;
            else:
                timePassed = cTime - pTime
                if timePassed > refreshTime:
                    keyboard.press_and_release("f5")
                    print("refresh page")
                    pTime = cTime
                print("time passed: {time:.2f}s".format(time = timePassed))

                time.sleep(1)

        # # fps
        # cTime = time.time()
        # fps = 1 / (cTime - pTime)
        # pTime = cTime
        # cv2.putText(imgRGB, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)

        # cv2.imshow('test', img2)


    cv2.imshow("Image", img)
    cv2.waitKey(1)

