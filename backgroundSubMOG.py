import numpy as np
import cv2

cap = cv2.VideoCapture('./videos/vtest.avi')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

WINDOW_ORG = "org"
#WINDOW_BACK = "back"
WINDOW_DIFF = "diff"
cv2.namedWindow(WINDOW_ORG)
#cv2.namedWindow(WINDOW_BACK)
cv2.namedWindow(WINDOW_DIFF)

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow(WINDOW_ORG,frame)
    cv2.imshow(WINDOW_DIFF,fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
