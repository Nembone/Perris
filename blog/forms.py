from django import forms

class RegistroForm(forms.Form):
    # variable o input que apareceran en la vista
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mascota = forms.CharField(max_length=100)