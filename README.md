# QR Generator

A simple Python project to generate QR code images from any website URL.

The program asks the user to enter a URL and a QR code file name. After generating the QR code, it automatically opens the saved image file.

## Features

* Generate QR codes from website URLs
* Choose your own QR image file name
* Save QR codes as PNG images
* Automatically open the generated QR code image
* Simple command-line program

## Requirements

* Python 3.x
* `qrcode` library
* Pillow library

## Installation

Open the terminal in VS Code and install the required library:

```bash
pip install qrcode[pil]
```

## How to Run

Open the project folder in VS Code.

Run the Python file using:

```bash
python "qr generator.py"
```

If that does not work, try:

```bash
py "qr generator.py"
```

## How to Use

1. Run the program.
2. Enter the website URL you want to convert into a QR code.
3. Enter a file name for the QR image.
4. Make sure to add `.png` at the end of the file name.
5. The QR code will be saved in the project folder.
6. The generated QR code image will open automatically.

## Example

```text
Enter Your URL : https://uniwallets.vercel.app
Enter QR file name : uniwallet.png
```

The generated file will be saved as:

```text
uniwallet.png
```

## Project Files

```text
QR-Generator/
├── qr generator.py
├── README.md
└── your-generated-qr.png
```

## Technologies Used

* Python
* qrcode
* Pillow
* os module

## Important Note

When entering the QR file name, use the `.png` extension.

Example:

```text
myqrcode.png
```

Do not enter only:

```text
myqrcode
```
