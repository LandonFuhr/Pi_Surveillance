from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
import imutils
import time
import cv2

def main():
    vs = PiVideoStream().start()
    time.sleep(2.0)
    fps = FPS().start()
    # loop over some frames...this time using the threaded stream
    while True:
        frame = vs.read()
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        fps.update()
        time.sleep(2)
    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

if __name__ == "__main__":
    main()