from django.shortcuts import render
import pyshorteners
import qrcode

def index(request):
    Link = None
    resultado = None 
    
    if request.method == "POST":
        # Obtiene los datos del formulario
        Link = request.POST.get('Link')
        art = pyshorteners.Shortener()
        resultado = (art.tinyurl.short(Link))


    return render(request, 'Index.html', {
        'resultado': resultado
    })

#img = qrcode.make(Acortado)
#type(img)
##img.save("QR.png")