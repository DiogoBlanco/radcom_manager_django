from django import forms
from clientes.models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
