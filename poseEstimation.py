import cv2
import numpy as np
import choosePoints


class poseEstimator:

    def drawBoxes(self, img, imgpts):
        imgpts = np.int32(imgpts).reshape(-1, 2)

        # draw ground floor in green
        img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)

        # draw pillars in blue color
        for i, j in zip(range(4), range(4, 8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)

        # draw top layer in red color
        img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)

        return img

    def estimate(self, camera_matrix, distortion_coefficients, img):

        # define the object points in 3D space
        objP = [[632, 217], [921, 361]]
        p1, p2 = objP[0], objP[1]

        obj_points = np.array([[p1[0], p1[1], 0], [p2[0], p1[1], 0], [p2[0], p2[1], 0], [p1[0], p2[1], 0]],
                              dtype=np.float32)

        # define the image points (the coordinates of the object points in the image)

        img_points = choosePoints.getImagePts(img, 'myImgage', 4)
        # calculate the rotation and translation vectors
        ret, rvec, tvec = cv2.solvePnP(obj_points, img_points, camera_matrix, distortion_coefficients)

        # project 3D points to image plane
        axisBoxes = np.float32([[p1[0], p1[1], 0], [p1[0], p2[1], 0],
                                [p2[0], p2[1], 0], [p2[0], p1[1], 0], [p1[0], p1[1], 300], [p1[0], p2[1], 300],
                                [p2[0], p2[1], 300], [p2[0], p1[1], 300]])

        # Project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axisBoxes, rvec, tvec, camera_matrix, distortion_coefficients)

        img = self.drawBoxes(img, imgpts)

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
