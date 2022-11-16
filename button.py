# import time
# import picamera
import RPi.GPIO as GPIO

from picamera import PiCamera
from time import sleep


button_pin = 27
camera = PiCamera()

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
# GPIO.setup(camera, GPIO.OUT)

buttonInputPrev = False
# cameraOn = False

try:
  while True:
    buttonInput = GPIO.input(button_pin)
    
    if buttonInput and not buttonInputPrev:
        print("rising edge")
        # cameraOn = Ture if not cameraOn else False
        # GPIO.output(camera, cameraOn)
        camera.start_preview()
        sleep(5)
        camera.capture('/home/jaehyeong/project/image/image.jpg')
        
        
        camera.stop_preview()
    elif not buttonInput and buttonInputPrev:
        print("falling edge")
    else: pass
    
    buttonInputPrev = buttonInput

except KeyboardInterrupt:
    pass
  
GPIO.cleanup()
# # with picamera.PiCamera() as camera:
# camera.start_preview()
# GPIO.wait_for_edge(27, GPIO.FALLING)
# camera.capture('/home/jaehyeong/project/image/image.jpg')
# camera.stop_preview()