import pyqrcode
import png
# Input data
data ="Hello"

# Create a QR code object
qr = pyqrcode.create(data)

# Save the QR code as a PNG image
qr.png("qrcode_pyqrcode.png", scale=6)

# You can also directly display the QR code
qr.show()
