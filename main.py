import cv2
import numpy

img = cv2.imread('./skull.jpg')
cv2.imshow('elmer', img)

def event_funct(event, x, y, flags, parms):
    if (event == cv2.EVENT_LBUTTONDOWN):
        print(x, y)
        cv2.circle(img, (x, y), 11, (0, 0, 255), thickness=3)
        text = str((x, y))
        print(text)
        cv2.putText(img, text, (x - 40, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), thickness=2)
        cv2.imshow('elmer', img)
        # It dosent matter how manny times you open the same window as long as it has the same window name

cv2.setMouseCallback('elmer', event_funct)
# This method allows to set a callback when an event has occured in the given window name
# and that callback will be called with the event and positions in X ,Y
# the given callback will be called everytime we click on the image window with that name

# The callback function need to have 5 essentials parameters

# event -> this will receive the kinf of event its happening, and we can use it to check if equals to one of the different
# types of events opencv has built in (cv2.EVENT_LBUTTONDOWN) (cv2.EVENT_RBUTTONDOWN) etc

# x -> its a number that will represent the point in the X axis where we clicked
# y -> its a number that will represent the point in hte Y axis where we clicked

# flags
# parms -> The parameters given in the setMouseCallback Method with the param=attributes


# cv2.setMouseCallback(windowName, callbackFunction, parms=)
# The window name where we will detect the events
# The callback that we are going to call when an event occurs
# The parameters we want to add to the callback, those parameters can be used in the callback with the last parameter parms

print('About to waitKey')
cv2.waitKey(0)
print('Again...')
# cv2.destroyAllWindows()