from django import forms
from .models import Annotation


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
