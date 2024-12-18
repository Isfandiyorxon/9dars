from .models import Gullar,Turlar
from django import forms

class GulForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        "placeholder":"Gul nomi",
        'class':"form-control"
    }))
    about=forms.CharField(required=False,widget=forms.Textarea(attrs={
        "placeholder": "Gul haqida",
        'class': "form-control",
        'rows':3
    }))
    photo=forms.ImageField(required=False,widget=forms.FileInput())
    tur=forms.ModelChoiceField(queryset=Turlar.objects.all(),
                                        widget=forms.Select(attrs={
                                            'class':'form-select'
                                        }))
    color=forms.CharField(max_length=13,widget=forms.TextInput(attrs={
        "placeholder": "Gul rangi",
        'class': "form-control"
    }))
    def create(self):
        gul= Gullar.objects.create(**self.cleaned_data)
        return gul

