import cv2
import numpy as np
import cv2 as cv

from choosePoints import *


class cameraCalibration:
    def __init__(self, images):
        self.images = images

################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################
    def run(self):

        chessboardSize = (24,17)
        chessboardSize = (300,400)
        frameSize = (1440,1080)

        # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
        objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

        size_of_chessboard_squares_mm = 20
        objp = objp * size_of_chessboard_squares_mm


        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.
        image = "images/chessboard.png"
        # for image in self.images:
        cv.namedWindow("img", cv.WINDOW_NORMAL)
        img = cv.imread(image)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
        # print(corners.type)


        getImagePts(gray, "windowPoints", 4)
        windowCorner = readWinodwCorners()

        ret = True
        # If found, add object points, image points (after refining them)
        if ret == True:

            objpoints.append(objp)
            # corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            corners2 = cv.cornerSubPix(gray, windowCorner, (11,11), (-1,-1), criteria)
            imgpoints.append(windowCorner)

            # Draw and display the corners
            cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
            cv.imshow('img', img)
            cv.waitKey(1000)


        cv.destroyAllWindows()


        ############## CALIBRATION #######################################################

        ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
        np.savez("CameraParams", cameraMatrix=cameraMatrix, dist=dist, rvecs=rvecs, tvecs=tvecs)


        # ############## UNDISTORTION #####################################################
        #
        # img = cv.imread('images/Image__2018-10-05__10-29-04.png')
        # h,  w = img.shape[:2]
        # newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))
        #
        #
        #
        # # Undisort
        # dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)
        #
        # # crop the image
        # x, y, w, h = roi
        # dst = dst[y:y+h, x:x+w]
        # cv.imwrite('caliResult1.png', dst)
        #
        #
        #
        # # Undistort with Remapping
        # mapx, mapy = cv.initUndistortRectifyMap(cameraMatrix, dist, None, newCameraMatrix, (w,h), 5)
        # dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
        #
        # # crop the image
        # x, y, w, h = roi
        # dst = dst[y:y+h, x:x+w]
        # cv.imwrite('caliResult2.png', dst)
        #
        #
        #
        #
        # # Reprojection Error
        # mean_error = 0
        #
        # for i in range(len(objpoints)):
        #     imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
        #     error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
        #     mean_error += error
        #
        # print("total error: {}".format(mean_error/len(objpoints)))
        #
