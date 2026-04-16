from django.urls import path
from .views import crear_solicitud

urlpatterns = [
    path('', crear_solicitud, name='crear_solicitud'),
]
