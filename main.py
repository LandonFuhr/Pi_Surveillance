import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 32
    camera.shutter_speed = 1000
    # Camera warm-up time
    time.sleep(2)
    print('capturing')
    camera.capture('foo.jpg')