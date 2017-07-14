from django import forms


class JoinForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)

