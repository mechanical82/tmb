from django import forms
from .models import CallbackRequest


class CallbackForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-50 form-control', 'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 999-99-99'}),
            'email': forms.EmailInput(attrs={'class': 'w-100 form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'cols': '30', 'rows': '10', 'placeholder': 'Ваше сообщение'})
        }


class CallbacktelegramForm(forms.Form):
    # fields = ['name', 'phone']
    # widgets = {
    #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
    #     'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 999-99-99'}),
    # }
    name = forms.CharField(label='Имя', max_length=100)
    phone = forms.CharField(label='Телефон', max_length=20)
    