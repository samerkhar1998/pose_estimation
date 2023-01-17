import glob
from cameraCalibration import *
from poseEstimation import *

if __name__ == '__main__':
    images = glob.glob('images/*.png')

    camera = cameraCalibration(images)
    camera.run()

    pose = poseEstimation(images)
    pose.run()
