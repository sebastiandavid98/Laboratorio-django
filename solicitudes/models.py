from django.db import models
# Validator para documento de identidad
from django.core.validators import RegexValidator

documento_validator = RegexValidator(
    regex=r'^[A-Za-z0-9]+$',
    message='El documento de identidad debe contener solo caracteres alfanuméricos.'
)


class Solicitud(models.Model):
    """Modelo para almacenar solicitudes."""

    # choices para tipo_solicitud
    TIPO_ACADEMICA = 'ACADEMICA'
    TIPO_ADMINISTRATIVA = 'ADMINISTRATIVA'
    TIPO_TECNICA = 'TECNICA'
    TIPO_OTRA = 'OTRA'

    TIPO_SOLICITUD_CHOICES = [
        (TIPO_ACADEMICA, 'Académica'),
        (TIPO_ADMINISTRATIVA, 'Administrativa'),
        (TIPO_TECNICA, 'Técnica'),
        (TIPO_OTRA, 'Otra'),
    ]

    nombre_solicitante = models.CharField('Nombre del solicitante', max_length=150)
    documento_identidad = models.CharField('Documento de identidad', max_length=50, validators=[documento_validator])
    correo = models.EmailField('Correo electrónico')
    # Campo numérico para teléfono de contacto (usar BigInteger para números largos)
    telefono = models.BigIntegerField('Teléfono de contacto')
    tipo_solicitud = models.CharField('Tipo de solicitud', max_length=20, choices=TIPO_SOLICITUD_CHOICES)
    asunto = models.CharField('Asunto', max_length=200)
    descripcion = models.TextField('Descripción')
    fecha_solicitud = models.DateField('Fecha de la solicitud')
    archivo_adjunto = models.FileField('Archivo adjunto', upload_to='solicitudes/adjuntos/', blank=True, null=True)

    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['-fecha_solicitud', '-created_at']

    def __str__(self):
        asunto_corto = (self.asunto[:50] + '...') if len(self.asunto) > 50 else self.asunto
        return f"{self.nombre_solicitante} — {self.get_tipo_solicitud_display()} — {asunto_corto}"
