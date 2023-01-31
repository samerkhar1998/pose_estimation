import glob
from cameraCalibration import *
from tryyyy import *
import cv2
from ReadFrames import readFrames
import yaml
from yaml.loader import SafeLoader
from poseEstimation import poseEstimator

if __name__ == '__main__':
    # Open the file and load the file
    with open("tello_camera.yaml", "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    camera_matrix = np.array(data['camera_matrix']['data']).reshape(data['camera_matrix']['rows'],
                                                                    data['camera_matrix']['cols'])

    distortion_coefficients = np.array(data['distortion_coefficients']['data']).reshape(
        data['distortion_coefficients']['rows'], data['distortion_coefficients']['cols'])

    estimate = poseEstimator()

    for image in glob.glob("images/*.png"):
        img = cv.imread(image)

        estimate.estimate(camera_matrix, distortion_coefficients, img)


    # cap = cv2.VideoCapture('images/1668941063944.mp4')
    # read = readFrames(cap)
    # read.read()
    # images = glob.glob('images/*.png')
    #
    # camera = cameraCalibration(images)
    # camera.run()

