import pyqrcode
import png
from pyqrcode import QRCode
# This will be converted into qr
print("Paste your text to convert")
s=input(": ")
# Name of file
print("Enter image name to save")
n=input(": ")
# Adding extension as .pnf
d=n+".png"
# Creates qr code
url=pyqrcode.create(s)
# Saves the file
url.show()
url.png(d, scale =6)
