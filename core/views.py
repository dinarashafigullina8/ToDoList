from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView

import core
from core.models import Doing


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class Doings(TitleMixin, ListView):

    def index(request):
        toDos = Doing.objects.all()
        return render(request, 'core/index.html', {"toDos": toDos})


class ToDoCreate(TitleMixin, CreateView):
    model = core.models.Doing
    form_class = core.forms.ToDoEdit
    title = 'Добавить дело'

    def get_success_url(self):
        return reverse('core:index')


