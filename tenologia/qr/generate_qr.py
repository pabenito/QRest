import qrcode
from qrcode.image.pure import PyPNGImage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask,

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    image_factory=PyPNGImage
)

qr.add_data('https://www.qrest.app/restaurante/pedidos/123456789')

img = qr.make_image()
img.save("qr.png")

img_style = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask(), embeded_image_path="icon.png")
img_style.save("qr_style.png")