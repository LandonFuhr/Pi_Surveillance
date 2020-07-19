import picamera
import time

def main():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('foo.jpg')

if __name__ == "__main__":
    main()