import qrcode as qr
img = qr.make("https://psarkar8585.github.io/sarkarpriti_portfolio/")
img.save("test.png")