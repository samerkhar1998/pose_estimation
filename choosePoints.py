import cv2
import numpy as np

# Load the image
from matplotlib import pyplot as plt

# img = cv2.imread("images/frame_2.png")
#
# # Create an empty list to store the points
# points = []
#
# # Use a for loop to select 4 points on the image
# for i in range(4):
#     print("Select point {} by clicking on the image.".format(i+1))
#     point = cv2.selectROI(img)
#     # Append the point to the list
#     points.append([point[0], point[1]])
#
# # Convert the list of points to a NumPy array
# points = np.array(points)
#
# # Save the array to an .npz file
# np.savez("points.npz", points=points)



def getImagePts(im1, varName1, nPoints):
    plt.figure()
    plt.imshow(im1, cmap='gray')
    plt.title("Original Image")
    Pts1 = plt.ginput(nPoints, 0)

    Pts1 = np.round(Pts1, 0)

    imagePts1 = np.ndarray((nPoints, 3), dtype=int)
    for i in range(nPoints):
        imagePts1[i] = np.append(Pts1[i], 1)
        curr = imagePts1[i][0]
        imagePts1[i][0] = imagePts1[i][1]
        imagePts1[i][1] = curr
    myPoints = []
    imagePts1 = imagePts1.round()
    for point in imagePts1:
        myPoints.append([point[1],point[0]])
    myPoints = np.array(myPoints, dtype=np.float32)
    return myPoints

def readWinodwCorners():
    corners3 = np.load('windowPoints.npy')
    corners3 = [[x, y] for x, y, z, in corners3]
    corners4 = np.ndarray((4, 1, 2))
    for corner1, corner2 in zip(corners4, corners3):
        corner1[0][0] = corner2[0]
        corner1[0][1] = corner2[1]
    return corners4

# #
# img = cv2.imread("images/frame_20.png")
# g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# getImagePts(g, "hello8", 4)