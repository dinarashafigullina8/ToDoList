from django.forms import ModelForm, TextInput

from core.models import Doing


class TodoCreateForm(ModelForm):
    class Meta:
        model = Doing
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите задание',
            'autofocus': 'true',
        })}