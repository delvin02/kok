from django.forms import ModelForm
from .models import IdentityRegister
from django import forms
from django.core.exceptions import ValidationError
from PIL import Image
import re

class IdentityRegisterForm(forms.ModelForm):
    
    class Meta:
        model = IdentityRegister
        fields = ['phone', 'front', 'back', 'selfie']
        labels = {
            'phone': 'Phone Number',
            'front': 'Gambar Depan IC',
            'back': 'Gambar Belakang IC',
            'selfie': 'Gambar Swafoto',
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'front': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*', 'capture': 'camera'}),
            'back': forms.FileInput(attrs={'class': 'form-control-file ', 'accept': 'image/*', 'capture': 'camera'}),
            'selfie': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*', 'capture': 'camera'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # This should be called after Meta, not before
        for field in self.fields.values():
            field.required = True

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not re.match(r'[\d\s\+\-\(\)]*$', phone):
            raise ValidationError("Phone number invalid.")
        return phone
    def clean_front(self):
        return self.clean_image_file('front')

    def clean_back(self):
        return self.clean_image_file('back')

    def clean_selfie(self):
        return self.clean_image_file('selfie')

    def clean_image_file(self, field_name):
        image_file = self.cleaned_data.get(field_name)
        if image_file:
            max_size = 5 * 1024 * 1024 
            if image_file.size > max_size:
                raise ValidationError(f"The {field_name} image file is too large ( > 5MB ). Please resize it and try again.")
            return image_file
        else:
            raise ValidationError(f"This field is required.")