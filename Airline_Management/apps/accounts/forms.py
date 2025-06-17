from django import forms
from .models import Account
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Nombre de Usuario',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password1 = forms.CharField(
        label='Contraseña',
        max_length=150,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    password2 = forms.CharField(
        label='Repite la Contraseña',
        max_length=150,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    email = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

    role_id = forms.CharField(
        label = 'Rol',
        widget=forms.Select(
            attrs={'class': 'form_control'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if Account.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya esta en uso')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise ValidationError('Este correo ya esta en uso')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('password2')

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('Las contraseñas no coinciden')
        
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de Usuario',
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password=forms.CharField(
        label='Contraseña',
        max_length=150,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )