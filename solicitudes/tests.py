from django.test import TestCase
from .models import Solicitud
from django.utils import timezone


class SolicitudModelTest(TestCase):
    def test_crear_solicitud_basica(self):
        s = Solicitud.objects.create(
            nombre_solicitante='Test User',
            documento_identidad='ABC123',
            correo='test@example.com',
            telefono=573001234567,
            tipo_solicitud=Solicitud.TIPO_ACADEMICA,
            asunto='Prueba',
            descripcion='Descripción de prueba',
            fecha_solicitud=timezone.now().date()
        )
        self.assertTrue(isinstance(s, Solicitud))
        self.assertEqual(str(s).split(' — ')[0], 'Test User')
