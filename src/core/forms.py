from django import forms


class HomeRquestForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'name', 'type': 'text'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'fname', 'type': 'text'}), label='')
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'phonenumber', 'type': 'text'}), label='')
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'explanation', 'type': 'text'}), label='')
