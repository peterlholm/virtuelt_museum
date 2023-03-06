"Generate QR pictures"

import qrcode


def qr_img(text):
    img = qrcode.make(text)
    type(img)
    img.save('test.png')

if __name__=="__main__":
    qr_img("test idag")
    