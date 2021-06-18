import cv2
import numpy

video = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
# cv2.CAP_DSHOW -> Allows to deal with the error of the cammera when is finished
# But we have to close the video capture (cv2.destroyAllWindows())


records = []

while True:
    ret, frame = video.read()

    if (len(records) != 0):
        for elm in records:
            cv2.circle(frame, elm, 3, (0, 0, 255), thickness=-1)
            cv2.putText(frame, str(elm), (elm[0] - 30, elm[1] + 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 0), thickness=1)

            

    cv2.imshow('Video', frame)

    def mouse_event(event, x, y, flags, parms):
        if (event == cv2.EVENT_LBUTTONDOWN):
            records.append((x, y))
            cv2.circle(frame, (x, y), 3, (0, 255, 0), thickness=-1)
            cv2.putText(frame, str((x, y)), (x - 30, y + 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 255), thickness=1)
            cv2.imshow('Video', frame)

    cv2.setMouseCallback('Video', mouse_event, param=['Elmer'])
    
    if (cv2.waitKey(20) == ord('q')):
        cv2.destroyAllWindows()
        break

