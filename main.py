import requests
import json
from requests_toolbelt import MultipartEncoder

url = "http://192.168.0.16:3003/camera/image"

headers = {
    # "Content-Type": "application/json"
    "Content-Type": "multipart/form-data"
}

# data = {
#   "name" : "kk"
# }

# data = json.dumps(data)

files = open('/home/jaehyeong/project/image/image.jpg', 'rb')
m = MultipartEncoder(fields = {'field0' : files})
upload = {'file3':m} 

print("이미지 : ",m)

res = requests.post(url,  headers={'Content-Type': m.content_type}, files = upload)
if res.status_code == 200:
     print("Success!!")
     print(type(files))
      
      
      
# def post(url, field_data) :
#     m = MultipartEncoder(fields=field_data)
#     headers = {'Content-Type' : m.content_type}
#     res = requests.post(url, headers=headers, data=m)
#     return res.status_code, res.json()