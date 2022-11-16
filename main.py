import requests
import json
from requests_toolbelt import MultipartEncoder


def photo_image(key):
    url = "http://192.168.0.16:3003/camera/image"

    payload = MultipartEncoder(
        fields={'key': key,
                'img' : ('image.jpg', open('image/image.jpg', 'rb'), 'text/plain'),
                }
    )

    # print(payload)
    
    res = requests.post(url, headers = {'Content-Type': payload.content_type}, data = payload)
    if res.status_code == 200:
             print("Success!!")
    
    
photo_image('1234')