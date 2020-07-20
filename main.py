import picamera
import time

with picamera.PiCamera() as camera:
    # Camera warm-up time
    time.sleep(2)
    print('capturing')
    camera.capture('foo.jpg')