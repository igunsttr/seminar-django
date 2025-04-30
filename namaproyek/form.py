from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Bukutamu

class Bukutamuform(forms.ModelForm):
    class Meta:
        model = Bukutamu
        fields = '__all__' 
