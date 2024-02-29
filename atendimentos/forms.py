from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = fields = ['customer', 'date',
                           'problem', 'solution', 'value', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
