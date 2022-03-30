from django.forms import ModelForm, TextInput, CheckboxInput
from core.models import models

import core.models


class TodoCreateForm(ModelForm):
    class Meta:
        model = core.models.Doing
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите задание',
            'autofocus': 'true',
        })}


class TodoCompletedForm(ModelForm):
    class Meta:
        model = core.models.Doing
        fields = ['name', 'completed']
        widgets = {
                   'name': TextInput(attrs={
                       'class': 'form-control',
                       'placeholder': 'Введите задание',
                       'autofocus': 'true',
                   }),
                   'completed': CheckboxInput(attrs={'class': 'form-check-input'})
                   }


class ToDoEdit(ModelForm):
    class Meta:
        model = core.models.Doing
        fields = '__all__'
