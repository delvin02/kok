from django.forms import ModelForm
from .models import Email


class ContactForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'