import qrcode

phone_number = "9805832889"  
message = "Sir Give me free django and AI course please "



sms_url = f"sms:{phone_number}?body={message}"

img = qrcode.make(sms_url)
type(img)  # qrcode.image.pil.PilImage



img.save("addrss.png")


print("QR code generated and saved successfully!")