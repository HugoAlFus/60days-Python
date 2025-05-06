import qrcode

data = "https://github.com/HugoAlFus"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("Hola mundo en código QR")
qr.make(fit=True)

img = qr.make_image(fill_color="dark", back_color="white")
img.save("personalizado.png")