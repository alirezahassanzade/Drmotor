from django import forms


class LoginForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'login text5', 'type': 'text5'}), label='')
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'password text5', 'type': 'password'}), label='')
