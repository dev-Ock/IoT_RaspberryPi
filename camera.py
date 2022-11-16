
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(15)
camera.capture('/home/jaehyeong/project/image/image7.jpg')
camera.stop_preview()