from django import forms
from crispy_forms.helper import FormHelper
from .models import Bukutamu
from django.core.validators import validate_email

class Bukutamuform(forms.ModelForm):
    class Meta:
        model = Bukutamu
        fields = '__all__' 


class Bukutamuform2(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(Bukutamuform2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  
        # required 
        self.fields['nama'].widget.attrs={'rows':1, 'cols':1}
        self.fields['email'].widget.attrs={'rows':1, 'cols':1}
        self.fields['pesan'].widget.attrs={'rows':5, 'cols':30}
        self.fields['hp'].widget.attrs={'rows':1, 'cols':1}


        self.fields['nama'].required = True
        self.fields['email'].required = True
        self.fields['hp'].required = True
        self.fields['jk'].required = True
        self.fields['pesan'].required = True 
        self.fields['id_jurusan'].required = True

    def clean(self):
            super(Bukutamuform2, self).clean()
            nama = self.cleaned_data.get('nama')
            email = self.cleaned_data.get('email')
            hp = self.cleaned_data.get('hp')
            pesan = self.cleaned_data.get('pesan')
            jk = self.cleaned_data.get('jk')
            id_jurusan = self.cleaned_data.get('id_jurusan')

            if len(nama) < 3 or len(nama) > 50:
                self._errors['nama'] = self.error_class(['Kolom Nama Minimal 3 huruf'])

            return self.cleaned_data 
    
    def validate(self, value):
        super(Bukutamuform2, self).validate(value)
        for email in value:
            validate_email(email)
    class Meta:
        model = Bukutamu
        fields = ('nama','email','hp','pesan','jk','id_jurusan')
