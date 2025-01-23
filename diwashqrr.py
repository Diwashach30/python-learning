import qrcode


qr_text = ""
img = qrcode.make(qr_text)
type(img)
img.save("DiwashQr.png")