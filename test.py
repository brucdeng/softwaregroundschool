import cv2
import numpy as np
import matplotlib.pyplot as plt
x = input("Enter file: ")
oldimg = cv2.imread(x)
img = cv2.resize(oldimg, (600,400))
HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
color_dict={"red":    [(np.array([0,120,70]),   np.array([10,255,255])),
               (np.array([170,120,70]), np.array([180,255,255]))],
    "orange": [(np.array([7,100,100]), np.array([20,255,255]))],
    "yellow": [(np.array([21,100,100]), np.array([35,255,255]))],
    "green":  [(np.array([36,100,100]), np.array([85,255,255]))],
    "blue":   [(np.array([86,100,100]), np.array([125,255,255]))]}
final={}
for color in color_dict:
    if color=="red":
        mask = cv2.bitwise_or(cv2.inRange(HSV_img,color_dict[color][0][0], color_dict[color][0][1]), cv2.inRange(HSV_img, color_dict[color][1][0], color_dict[color][1][1]))
    else:
        mask = cv2.inRange(HSV_img, color_dict[color][0][0], color_dict[color][0][1])
    result = cv2.bitwise_and(img, img, mask=mask)
    final[color]=result
    cv2.imshow(color, result)



cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()