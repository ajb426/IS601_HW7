import qrcode
import os

def generate_qr(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    print(f"QR code generated and saved to {file_path}")

if __name__ == "__main__":
    qr_data = os.getenv('QR_DATA_URL', 'https://github.com/yourusername')
    qr_file_path = os.getenv('QR_CODE_FILENAME', 'qr_code.png')
    print(f"Generating QR code for URL: {qr_data}")
    generate_qr(qr_data, qr_file_path)
    print("QR code generation complete.")
