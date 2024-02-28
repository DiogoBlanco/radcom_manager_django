from django import forms
from .models import Customer, File


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
