from django import forms
from django.forms import ModelForm
from app.models import Televisores, Notebooks, Celulares


class CreateTv(ModelForm):
    #nombre = forms.CharField(max_length=40)
    #precio = forms.DecimalField(max_digits=15, decimal_places=None)
    #image = forms.ImageField()

    class Meta:
        model = Televisores
        fields = [
            'nombre',
            'precio',
            'image'
        ]


class CreatePhone(ModelForm):
    #nombre = forms.CharField(max_length=40)
    #precio = forms.DecimalField(max_digits=15, decimal_places=2)
    #image = forms.ImageField()

    class Meta:
        model = Celulares
        fields = [
            'nombre',
            'precio',
            'image'
        ]


class CreateLaptop(ModelForm):
    #nombre = forms.CharField(max_length=40)
    #precio = forms.DecimalField(max_digits=15, decimal_places=2)
    #image = forms.ImageField()

    class Meta:
        model = Notebooks
        fields = [
            'nombre',
            'precio',
            'image'
        ]