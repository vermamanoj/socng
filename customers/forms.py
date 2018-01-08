# THis form is not in use as of now

from django import forms
from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'mode', 'location', 'vertical']


