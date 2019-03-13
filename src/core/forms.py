from django import forms


class LoginForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'login text5', 'type': 'text5'}), label='')
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'password text5', 'type': 'password'}), label='')


class SignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'login text5', 'type': 'text2'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'text5', 'type': 'familyname'}), label='')
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'login text5', 'type': 'text3'}), label='')
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'login text5', 'type': 'text4'}), label='')


class HomeRquestForm(forms.Form):
    pass
