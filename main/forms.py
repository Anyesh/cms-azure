from django import forms
from .models import Container, Country


class AddContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['cid', 'country']

        widgets = {
        'cid': forms.TextInput(attrs={'placeholder': 'CID', 'class': 'form-control', 'id': '_cid'}),

        # 'unit': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ou', 'onkeyup': 'balance_total_calc()'}),
        # 'rate': forms.NumberInput(attrs={'class': 'form-control', 'id': 'or', 'onkeyup': 'balance_total_calc()'}),
        }


class AddCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['title']
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Country Name', 'class': 'form-control'}),

        }
