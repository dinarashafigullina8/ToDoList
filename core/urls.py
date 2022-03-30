from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.Todo.index, name='index'),
    path('doing/<int:pk>/', core.views.Todo.detail, name='doing_detail'),
    path('doing/create', core.views.Todo.create, name='doing_create'),
    path('doing/<int:pk>/update/', core.views.Todo.update, name='doing_update'),
    path('doing/<int:pk>/delete/', core.views.Todo.delete, name='doing_delete'),

]