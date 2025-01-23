import qrcode

phone_number = "9805832889"  
message = "Sir Give me free django and AI course please "

# Ensure the message is URL-encoded to handle spaces and special characters
import urllib.parse
encoded_message = urllib.parse.quote(message)

sms_url = f"sms:{phone_number}?body={encoded_message}"

img = qrcode.make(sms_url)

img.save("sms_qr_code.png")

print("QR code generated and saved successfully!")