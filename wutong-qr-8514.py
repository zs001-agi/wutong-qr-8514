import argparse
from qrcode import QRCode, constants

def generate_qr_code(data, output):
    if not data:
        print("Error: No data provided.")
        return

    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(output)

def read_qr_code(image):
    try:
        qr = QRCodeReader()
        result = qr.decode(image)
        return result
    except Exception as e:
        print(f"Error decoding QR code: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR code generator/reader CLI tool.")
    subparsers = parser.add_subparsers()

    # Generate QR Code Command
    generate_parser = subparsers.add_parser("generate", help="Generate a QR code from data.")
    generate_parser.add_argument("data", type=str, help="Data to encode in the QR code.")
    generate_parser.add_argument("--output", required=True, help="Output file for the QR code image.")
    generate_parser.set_defaults(func=generate_qr_code)

    # Read QR Code Command
    read_parser = subparsers.add_parser("read", help="Read a QR code from an image and print its data.")
    read_parser.add_argument("image", type=str, help="Image file containing the QR code to decode.")
    read_parser.set_defaults(func=read_qr_code)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(**vars(args))