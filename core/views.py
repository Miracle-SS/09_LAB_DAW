from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.core.mail import send_mail
def home(request):
    return HttpResponse("Laboratorio 09")
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        data = {
            'invoice_id': 12345,
            'customer_name': 'Carlo Corrales',
            'amount': 500.00,
        }
        pdf = render_to_pdf(
            'invoice.html',
            data
        )
        if pdf:
            return pdf
        return HttpResponse(
            'Error al generar PDF'
        )

def enviar_correo_vista(request):

    if request.method == 'POST':

        subject = request.POST.get('subject')

        message = request.POST.get('message')

        send_mail(
            subject,
            message,
            'admin@gmail.com',
            ['destino@gmail.com'],
            fail_silently=False
        )

        return HttpResponse(
            'Correo enviado correctamente'
        )

    return render(
        request,
        'contacto.html'
    )