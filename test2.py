import qrcode
qr=qrcode.QRCode(
    version=15, #qrcodesize
    box_size=10,
    border=5
)
data='https://psarkar8585.github.io/sarkarpriti_portfolio/'
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="red",back_color='white')
img.save("test3.png")
