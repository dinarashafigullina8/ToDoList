from django import forms
from core.models import models

import core.models


class ToDoFilter(forms.Form):
    name = forms.CharField(label='Название', required=False)


class ToDoEdit(forms.ModelForm):
    class Meta:
        model = core.models.Doing
        fields = '__all__'
