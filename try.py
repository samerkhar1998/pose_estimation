import cv2
import numpy as np
import yaml

import choosePoints


def drawBoxes(img, imgpts):
    imgpts = np.int32(imgpts).reshape(-1, 2)

    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)

    # draw pillars in blue color
    for i, j in zip(range(4), range(4, 8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)

    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)

    return img


img = cv2.imread("images/frame_2.png")

with open("tello_camera.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

camera_matrix = np.array(data['camera_matrix']['data']).reshape(data['camera_matrix']['rows'],
                                                                data['camera_matrix']['cols'])

distortion_coefficients = np.array(data['distortion_coefficients']['data']).reshape(
    data['distortion_coefficients']['rows'], data['distortion_coefficients']['cols'])

# define the object points in 3D space
'''

'''
objP = [[632, 217], [921, 361]]
p1, p2 = objP[0], objP[1]

obj_points = np.array([[p1[0], p1[1], 0], [p2[0], p1[1], 0], [p2[0], p2[1], 0], [p1[0], p2[1], 0]], dtype=np.float32)

# define the image points (the coordinates of the object points in the image)
img_points = np.array([[632, 217], [921, 217], [921, 361], [632, 361]], dtype=np.float32)
# img_points = np.array([[593, 353], [1019, 353], [1019, 568], [593, 568]], dtype=np.float32)
# img_points = np.array([[616, 242], [921, 242], [921, 408], [616, 408]], dtype=np.float32)
# img_points = np.array([[575 , 41], [859 , 41], [859 , 196], [575 , 196]], dtype=np.float32)

img_points = choosePoints.getImagePts(img,'myImgage', 4)
# calculate the rotation and translation vectors
ret, rvec, tvec = cv2.solvePnP(obj_points, img_points, camera_matrix, distortion_coefficients)

# project 3D points to image plane
axisBoxes = np.float32([[p1[0], p1[1], 0], [p1[0], p2[1], 0],
                        [p2[0], p2[1],0], [p2[0], p1[1], 0], [p1[0], p1[1], 300], [p1[0], p2[1], 300],
                         [p2[0], p2[1],300], [p2[0], p1[1], 300]])

# Project 3D points to image plane
imgpts, jac = cv2.projectPoints(axisBoxes, rvec, tvec, camera_matrix, distortion_coefficients)

img = drawBoxes(img, imgpts)

cv2.imshow('img', img)

k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('pose', img)

cv2.destroyAllWindows()

print("rotation Vector:")
print(rvec)
print("-------")
print("transaltion vector:")
print(tvec)
