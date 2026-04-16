from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento (alfanumérico)'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '3000000000'}),
            'tipo_solicitud': forms.Select(attrs={'class': 'form-select'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto breve'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describa la solicitud'}),
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
