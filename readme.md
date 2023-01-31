## poseEstimation file:

### Introduction
This repository contains code for the pose estimation of an object using OpenCV's SolvePnP function. The pose estimation algorithm takes an image of an object, the camera matrix and distortion coefficients, and estimates the 3D orientation and position of the object in the image.
### Requirements
* Python 3
* OpenCV
* numpy
* yaml

### Note
The camera matrix and distortion coefficients are expected to be in a YAML file named "tello_camera.yaml" in the same directory as the code.
The image points (2D coordinates of the object in the image) are currently hardcoded in the code, this should be updated to use a function that returns the image points, such as the function choosePoints.getImagePts mentioned in the code.

### Conclusion
This code provides a basic implementation of pose estimation using the SolvePnP function in OpenCV. It can be used as a starting point for developing more advanced pose estimation algorithms.
