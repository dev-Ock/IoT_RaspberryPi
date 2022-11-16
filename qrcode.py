import qrcode

img_url = '/home/jaehyeong/project/image/image7.jpg'
# qr_gen = qrcode.make(img_url)
# qr_gen.save("qrcode7.png")
# print(qr_gen.size)

img_url = "https://blog.naver.com/dsz08082"
qr_gen = qrcode.make(img_url)
qr_gen.save("myblog.png")
print(qr_gen.size)