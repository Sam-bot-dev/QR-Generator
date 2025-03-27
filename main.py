import qrcode
from PIL import Image
import base64
from io import BytesIO

# Step 1: Load your image and convert it to base64
image_path = "test-image.jpg"  # Replace with your image path
with open(image_path, "rb") as img_file:
    # Convert image to base64
    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# Step 2: Generate a QR code with the base64 string
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border
)

# Add the base64-encoded image data to the QR code
qr.add_data(img_base64)
qr.make(fit=True)

# Step 3: Create an image from the QR code
qr_img = qr.make_image(fill='black', back_color='white')

# Save the QR code as a PNG image
qr_img.save("image_to_qr_code.png")

# Show the QR code (optional)
qr_img.show()
