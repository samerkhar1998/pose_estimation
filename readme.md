## poseEstimation file:

This code defines a class called "poseEstimation" which takes a list of images as input. The class has a single method called "run" which performs pose estimation on the provided images.

The method starts by loading previously saved camera parameters from a file called 'CameraParams.npz' using the numpy function 'np.load'. These parameters include the camera matrix, distortion coefficients, rotation vectors, and translation vectors.

The code then defines two helper functions, "draw" and "drawBoxes". The "draw" function takes an image, corners, and image points as input, and draws lines connecting the first corner of the chessboard to the first, second, and third image points. The "drawBoxes" function takes an image, corners, and image points as input, and draws a green box representing the ground floor, blue lines representing the pillars, and a red box representing the top layer of the chessboard.

The script then sets up termination criteria for the corner detection algorithm, creates an array of 3D object points corresponding to the chessboard corners, and an array of axis points.

It then loops through all the images provided in the constructor and uses the OpenCV function 'findChessboardCorners' to detect the corners of a chessboard in the image. If corners are found, the script refines the corners, finds the rotation and translation vectors using the 'solvePnP' function, and projects the 3D points onto the image plane. The script then calls the "drawBoxes" function to draw the boxes on the image, and shows the image.

The script also allows user to save images on pressing 's' key.

Finally, the script closes all the open windows.

## cameraCallibration file:

1. The class first initializes a chessboard pattern of size 24x17 and sets the termination criteria for corner detection.
2. It then creates an array of object points corresponding to the chessboard pattern and another array to store the image points.
3. For each image in the input list, the class finds the chessboard corners in the image and adds the object points and corresponding image points to the arrays.
4. Then it uses the object points and image points arrays to calibrate the camera using the cv2.calibrateCamera() function, which returns the camera matrix, distortion coefficients, rotation and translation vectors.
5. The class then saves the camera matrix and distortion coefficients to a file called "CameraParams.npz"
6. After that, it undistorts an image using the cv2.undistort() function with the obtained camera matrix and distortion coefficients, and saves the result to an image file.
7. It also undistorts the image by remapping it with cv2.remap() function, and saves the result to another image file.
8. Finally, it calculates the reprojection error using the cv2.projectPoints() function and the obtained rotation and translation vectors, and prints the mean error.
