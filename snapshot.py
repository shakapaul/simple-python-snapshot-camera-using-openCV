#!/usr/bin/env python

"""
SNAPS Is simple Toolfor Taking Snapshots From A WebCam.
The Images Are Saved In Current Directory Named According
To The Time They Were Taken. Including Date and Year....

Usage:
    Press 's' To TAKE SnapShot.
    Press 'q' To QUIT.
"""


import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    ret, video = cap.read()
    cv2.imshow('SNAPS', video)
    key  = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        now = time.asctime()
        cv2.imwrite(str(now) + '.jpg', video)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

