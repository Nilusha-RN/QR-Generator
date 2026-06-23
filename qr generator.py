import qrcode

url = input("Enter Your URL : ") .strip()
file_path = "F:\\Bussiness\\Project\\QR python\\qr.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
