from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def crear_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia.html', {'form': form})