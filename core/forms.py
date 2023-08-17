from django import forms

class Contact(forms.Form):
    nombre = forms.CharField(label='Nombre y Apellido')
    correo = forms.EmailField(label='Tu correo electronico')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)