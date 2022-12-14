import qrcode
import cv2
from PIL import Image

features=qrcode.QRCode(version=2,box_size=40,border=3)

features.add_data('https://www.tcetmumbai.in/deptEXTC_home.html')
features.make(fit=True)

generator=features.make_image(fill_color='black',back_color='white')

generator.save("image3.png")



img = cv2.imread("image3.png")
img = Image.fromarray(img, "RGB")
img.show()