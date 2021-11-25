from django import forms
from django.forms import fields
from .models import Tarea
class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ['tarea']