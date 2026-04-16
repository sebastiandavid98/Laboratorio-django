from django.shortcuts import render
from .forms import SolicitudForm


def crear_solicitud(request):
    mensaje = None
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = 'Solicitud enviada correctamente.'
            form = SolicitudForm()
        else:
            mensaje = 'Por favor corrige los errores en el formulario.'
    else:
        form = SolicitudForm()

    return render(request, 'solicitudes.html', {'form': form, 'mensaje': mensaje})
