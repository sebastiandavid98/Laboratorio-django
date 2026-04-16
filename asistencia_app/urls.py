from django.urls import path
from .views import crear_asistencia

urlpatterns = [
    path('', crear_asistencia, name='crear_asistencia'),
]