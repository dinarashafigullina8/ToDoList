from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, FormView

from core.forms import TodoCreateForm
from core.models import Doing

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class Todo(LoginRequiredMixin, ListView):
    model = Doing
    fields = '__all__'
    template_name = 'core/index.html'
    form_class = TodoCreateForm
    context_object_name = 'todos'

    def create(request):

        if request.method == 'POST':
            form = TodoCreateForm(request.POST)
            form.instance.user = request.user
            form.save()
            return redirect('/')
        else:
            return redirect('/')

    def delete(request, pk):
        todo = Doing.objects.get(pk=pk)
        todo.delete()
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoCreateForm()
        context['todos'] = context['todos'].filter(user=self.request.user)
        context['count'] = context['todos'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['todos'] = context['todos'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Doing
    fields = '__all__'
    success_url = reverse_lazy('core:todos')


class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('core:todos')


class RegisterPage(FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('core:todos')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:todos')
        return super(RegisterPage, self).get(*args, **kwargs)
