from django.shortcuts import redirect


def index(request):
    return redirect('/admin/solicitudes/solicitud/add/')
