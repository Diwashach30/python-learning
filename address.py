import qrcode


phone_number = "9845320017"  
message = "Babe I Love You"


sms_url = f"sms:{phone_number}?body={message}"

qr = qrcode.make(sms_url)

qr.save("sms_qr_code.png")

print("QR code generated and saved as sms_qr_code.png")
