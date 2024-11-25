from symtable import Class

from django import forms
from myapp.models import Appointments, ImageModel


class AppointmentsForm(forms.ModelForm):
    class Meta:
         model = Appointments
         fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'