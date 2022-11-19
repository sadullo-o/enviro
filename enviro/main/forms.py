from django import forms
from .models import Contact, Orders


class AddContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'number', 'email']


class AddOrders(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'number', 'email', 'p_title', 'p_body']
