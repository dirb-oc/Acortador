from django.shortcuts import render
import pyshorteners
import qrcode
# Create your views here.

Link = input("Escribe el link: ")
s = pyshorteners.Shortener()
Acortado = (s.tinyurl.short(Link))
print(Acortado)

img = qrcode.make(Acortado)
type(img)
##img.save("QR.png")