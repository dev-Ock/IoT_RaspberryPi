import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

import requests
import json
from requests_toolbelt import MultipartEncoder

# def main_page():
#     url = "http://192.168.0.16:3003"
#     res = requests.get(url)
#     if res.status_code == 200:
#           print("main_page")

def photo_image(key):
    print("들어옴")
    url = "http://192.168.0.16:3003/camera/image"
           
    payload = MultipartEncoder(
        fields={'key': key,
                'img' : ('image.jpg', open('image/image.jpg', 'rb'), 'text/plain'),
                }
    )
    print("들어옴2")
    
    res = requests.post(url, headers = {'Content-Type': payload.content_type}, data = payload)
    if res.status_code == 200:
             print("Success!!")
             
button_pin = 27
camera = PiCamera()
# camera.rotation = 180

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)

buttonInputPrev = False

try:
  while True:
    buttonInput = GPIO.input(button_pin)
    
    if buttonInput and not buttonInputPrev:
        print("rising edge")
        camera.start_preview()
        sleep(2)
        camera.capture('/home/jaehyeong/project/image/image.jpg')
        camera.stop_preview()
        photo_image('1234')
        
    elif not buttonInput and buttonInputPrev:
        # main_page()      
        print("falling edge")
    else: pass
    
    buttonInputPrev = buttonInput

except KeyboardInterrupt:
    pass
  
GPIO.cleanup()
