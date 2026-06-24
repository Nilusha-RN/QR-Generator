import qrcode
import os

url = input("Enter Your URL : ") .strip()
file_name = input("Enter QR file name : ").strip()
folder_path = "F:\Bussiness\Project\QR\QR python"
file_path = os.path.join(folder_path, file_name)

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

os.startfile(file_path)  
