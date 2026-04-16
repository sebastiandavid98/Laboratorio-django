from django.shortcuts import render, redirect
from django.contrib import messages

from solicitudes.forms import SolicitudForm


def index(request):
    """Mostrar el formulario de Solicitud en la página principal y procesar envíos."""
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud enviada correctamente.')
            return redirect('home')
        else:
            messages.error(request, 'Hay errores en el formulario, por favor revise los campos.')
    else:
        form = SolicitudForm()

    return render(request, 'main/index.html', {'form': form})
