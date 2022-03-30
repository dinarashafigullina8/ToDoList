from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import core.forms
import core.filters
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

    def get_filters(self):
        return core.filters.DoingFilter(self.request.GET)

    def index(request):
        toDos = Doing.objects.all()
        return render(request, 'core/index.html', {"toDos": toDos})


class DoingUpdate(TitleMixin, UpdateView):
    model = core.models.Doing
    form_class = core.forms.ToDoEdit

    def get_title(self):
        return f'Изменение данных книги "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('core:index')


class DoingCreate(TitleMixin, CreateView):
    model = core.models.Doing
    form_class = core.forms.ToDoEdit
    title = 'Добавление книги'

    def get_success_url(self):
        return reverse('core:index')


class DoingDelete(TitleMixin, DeleteView):
    model = core.models.Doing

    def get_title(self):
        return f'Удаление книги {str(self.get_object())}'

    def get_success_url(self):
        return reverse('core:index')
