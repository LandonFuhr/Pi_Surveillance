from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
import imutils
import time
import cv2

def main():
    targetFramerate = 20

    sleepLength = 1/targetFramerate
    vs = PiVideoStream().start()
    time.sleep(2.0)
    fps = FPS().start()
    # loop over some frames...this time using the threaded stream
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=1800)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        fps.update()
        if key == ord('q'):
            break
        time.sleep(sleepLength)
    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

if __name__ == "__main__":
    main()