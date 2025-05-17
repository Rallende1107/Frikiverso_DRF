from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    fono = forms.CharField(label="Teléfono", max_length=15)
    correo = forms.EmailField(label="Correo")
    asunto = forms.CharField(label="Asunto", max_length=150)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)
