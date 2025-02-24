import qrcode
import qrcode.constants

konumBaglanti = "https://earth.google.com/web/search/k%c4%b1z+kulesi/@41.0211414,29.0041309,-0.1886387a,619.00878801d,35y,0h,0t,0r/data=CnoaTBJGCiUweDE0Y2FiODM5NTU1NTU1NTU6MHhjZDAwM2M4ZDhhZTRkNzJlGQLAZ9q0gkRAIdmQf2YQAT1AKgtrxLF6IGt1bGVzaRgCIAEiJgokCaxR6Ja750NAEa1R6Ja750PAGeQfIJaB4UxAIeQfIJaB4UzAQgIIAToDCgEwQgIIAEoNCP___________wEQAA"

qr = qrcode.QRCode(
   version=1,
   error_correction=qrcode.constants.ERROR_CORRECT_L,
   box_size=15,
   border=7,
)

qr.add_data(konumBaglanti)
qr.make(fit=True)

qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save("konum.qr.png")
qr_image.show()
