from picamera import PiCamera
import time
import cv2

def main():
    with PiCamera() as camera:
        camera.resolution = (1024, 768)
        time.sleep(2)
        for frame in camera.capture_continuous():
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

if __name__ == "__main__":
    main()