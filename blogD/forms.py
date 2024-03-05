from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput,\
    EmailInput, PasswordInput, DateInput
from .models import Profile, Author, Post
from django.contrib.auth.models import User



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "First name"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Last name",
            }),
            "username": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Username",
                "aria-describedby": "addon-wrapping",
            }),
            "email": EmailInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "E-mail",
                "aria-describedby": "inputGroup-sizing-default",
            }),
            "password": PasswordInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Password",
                "aria-describedby": "inputGroup-sizing-default",
            }),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'description', 'birth_data', 'phone']
        widgets = {
            'image': FileInput(attrs={
                'style': 'width: 145px; margin: 40px;',
                'class': 'form-control',
                'placeholder': 'Изображение',
            }),
            'description': Textarea(attrs={
                "rows": "6",
                'class': 'form-control',
                'placeholder': 'О себе!',
            }),
            'birth_data': DateInput(attrs={
                'class': 'form-control',
                'min': '1900-01-01',
                'placeholder': 'Дата рождения',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
            })
        }