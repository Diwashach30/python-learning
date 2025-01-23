import qrcode

qr_text = "TEL : 9845646222"

img = qrcode.make(qr_text)
type(img)

img.save("phone.png")
print ("QR image Saved")


