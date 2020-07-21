from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
import imutils
import time
import cv2

def main():
    targetFramerate = 20

    sleepLength = 1/targetFramerate
    vs = PiVideoStream(resolution=(640,480), vflip=True).start()
    time.sleep(2.0)
    fps = FPS().start()
    # loop over some frames...this time using the threaded stream
    capture = True
    try:
        while capture:
            frame = vs.read()
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            fps.update()
            if key == ord('q'):
                capture = False
            # time.sleep(sleepLength)

        # on break
        fps.stop()
        print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    finally:
        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()

if __name__ == "__main__":
    main()