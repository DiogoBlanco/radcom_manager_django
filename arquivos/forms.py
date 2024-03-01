from django import forms
from .models import Files


class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['backup_pabx'].required = False
            self.fields['backup_rb'].required = False
