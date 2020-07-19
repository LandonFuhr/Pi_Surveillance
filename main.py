import picamera
import time

with picamera.PiCamera() as camera:
    print('main')
    camera.shutter_speed = 1000
    camera.resolution = (1024, 768)
    # Camera warm-up time
    time.sleep(2)
    print('capturing')
    camera.capture('foo.jpg')