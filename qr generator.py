import qrcode
import os

url = input("Enter URL: ").strip()

if not url:
    print("URL cannot be empty.")
    exit()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

file_name = input("Enter QR file name: ").strip()

if not file_name:
    print("Filename cannot be empty.")
    exit()

if not file_name.endswith(".png"):
    file_name += ".png"

folder_path = "F:\Bussiness\Project\QR\QR python"
file_path = os.path.join(folder_path, file_name)

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

os.startfile(file_path)  