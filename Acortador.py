import pyshorteners
import qrcode

Link = input("Escribe el link: ")
s = pyshorteners.Shortener()
print(s.tinyurl.short(Link))

img = qrcode.make(Link)
type(img)
img.save("QR.png")