
import qrcode
from PIL import Image

def create_qr_code(image_path, output_path):
    # Create QR code instance with optimal settings for images
    qr = qrcode.QRCode(
        version=None,  # Auto-determine version
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction for images
        box_size=10,
        border=4,
    )
    
    # Read the image in binary mode
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    # Add the binary data to QR code
    qr.add_data(image_data)
    qr.make(fit=True)
    
    # Create the QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code
    qr_image.save(output_path)
    print(f"QR code saved as {output_path}")
    
    return qr_image

# Generate QR code from the image
input_image = "test-image.jpg"
output_qr = "qr_code_output.png"

try:
    qr_image = create_qr_code(input_image, output_qr)
    qr_image.show()  # Display the QR code
except Exception as e:
    print(f"Error generating QR code: {e}")
