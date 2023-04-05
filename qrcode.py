import pyqrcode
import png
link = "https://www.youtube.com/channel/UCgt8D6YwX8lDjuEA9NNnWng"
qr_code = pyqrcode.create(link)
qr_code.png("youtube.png", scale=5)