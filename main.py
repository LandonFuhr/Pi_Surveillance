import picamera
import time

def main():
    with picamera.PiCamera() as camera:
        print('main')
        camera.shutter_speed = 1000
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        print('capturing')
        camera.capture('foo.jpg')

if __name__ == "__main__":
    main()