# QR Generator

A simple Python application that generates customizable QR codes from website URLs. The project includes input validation, customizable QR settings, color selection, QR generation history, and automatic opening of the generated image.

## Features

* Generate QR codes from website URLs
* Automatic URL validation (`https://` is added if missing)
* Custom QR Version (1–40)
* Custom Box Size
* Custom Border Size
* Custom QR color
* Custom background color
* Automatically creates an output folder
* Saves QR codes as PNG images
* Stores QR generation history with date and time
* Automatically opens the generated QR code
* Simple command-line interface

## Requirements

* Python 3.x
* qrcode
* Pillow

## Installation

Clone the repository:

```bash
git clone https://github.com/Nilusha-RN/QR-Generator.git
cd QR-Generator
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install qrcode[pil]
```

## How to Run

Run the application:

```bash
python "qr generator.py"
```

or

```bash
py "qr generator.py"
```

## How to Use

1. Enter the website URL.
2. Enter a name for the QR code image.
3. Select the QR Version (Recommended: **1–5**).
4. Select the Box Size (Recommended: **8–12**).
5. Select the Border Size (Recommended: **2–4**).
6. Choose the QR code color.
7. Choose the background color.
8. The QR code will be generated and saved inside the **output** folder.
9. The generated image will open automatically.
10. The QR generation details will be saved in **history.txt**.

## Example

```text
Enter URL: google.com
Enter QR file name: google.png

Enter QR Version (1-40) [Recommended: 1-5]: 2
Enter Box Size [Recommended: 8-12]: 10
Enter Border Size [Recommended: 2-4]: 4

QR Color: blue
Background Color: white
```

## Technologies Used

* Python
* qrcode
* Pillow
* os
* datetime

## Future Improvements

* Add support for QR codes containing text, email addresses, phone numbers, and Wi-Fi credentials.
* Add a logo to the center of the QR code.
* Build a graphical user interface (GUI) using Tkinter.
* Create a web version using Flask or Streamlit.
* Export QR history as a CSV file.

## License

This project is created for learning and educational purposes.
