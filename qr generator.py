import qrcode
import os
from datetime import datetime

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

folder_path ="F:\\Bussiness\\Project\\QR\\QR python"
file_path = os.path.join(folder_path, file_name)

version = int(input("Enter QR Version (1-40) [Recommended: 1-5]: "))
box_size = int(input("Enter Box Size [Recommended: 8-12]: "))
border = int(input("Enter Border Size [Recommended: 2-4]: "))

qr = qrcode.QRCode(
    version=version,
    box_size=box_size,
    border=border
)
qr.add_data(url)

fill = input("QR Color: ")
back = input("Background Color: ")

img = qr.make_image(
    fill_color=fill,
    back_color=back
)
img.save(file_path)

with open("history.txt", "a") as file:
    file.write(
        f"{datetime.now():%Y-%m-%d %H:%M:%S} | {url} | {file_name}\n"
    )

print("\n========== QR History ==========")

if os.path.exists("history.txt"):
    with open("history.txt", "r") as file:
        print(file.read())

os.startfile(file_path)  

