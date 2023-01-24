import cv2


class readFrames():
    def __init__(self, cap):
        self.cap = cap

    def read(self):


        # Get the frame rate
        fps = self.cap.get(cv2.CAP_PROP_FPS)

        # Get the total number of frames
        total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Create a list to store the frames
        frames = []

        # Extract one frame per second
        for i in range(total_frames):
            ret, frame = self.cap.read()
            if ret == True:
                if i % int(fps) == 0:
                    frames.append(frame)
            else:
                break

        # Release the video capture object
        self.cap.release()

        # Do something with the frames
        for i, frame in enumerate(frames):
            cv2.imwrite("newImages/frame_" + str(i) + ".jpg", frame)