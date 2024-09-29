import qrcode
import base64
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    qr_image_url = None

    if request.method == "POST":
        link = request.POST.get('Link')
        
        # Generar el código QR
        img = qrcode.make(link)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Codificar la imagen a base64
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        qr_image_url = f"data:image/png;base64,{img_base64}"

    return render(request, 'index.html', {
        'qr_image_url': qr_image_url,
    })