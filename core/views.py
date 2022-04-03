from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView


from core.forms import TodoCompletedForm, TodoCreateForm
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


class Todo(TitleMixin, ListView):

    def get_filters(self):
        return core.filters.DoingFilter(self.request.GET)

    def index(request):
        form = TodoCreateForm()
        todos = Doing.objects.all()
        context = {
            'todos': todos,
            'form': form
        }
        return render(request, 'core/index.html', context)

    def create(request):
        if request.method == 'POST':
            form = TodoCreateForm(request.POST)
            form.save()
            return redirect('/')
        else:
            return redirect('/')

    def update(request, pk):
        todo = Doing.objects.get(pk=pk)
        form = TodoCompletedForm(instance=todo)

        if request.method == 'POST':
            form = TodoCompletedForm(request.POST, instance=todo)
            form.save()
        return redirect('/')

    def delete(request, pk):
        todo = Doing.objects.get(pk=pk)
        todo.delete()
        return redirect('/')




def book_detail(request, pk):
    book = get_object_or_404(core.models.Doing, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})


class TodoUpdate(UpdateView):
    model = Doing
    fields = '__all__'
    success_url = reverse_lazy('core:todos')
