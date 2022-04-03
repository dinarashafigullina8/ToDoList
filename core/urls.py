from django.urls import path
import core.views
from django.contrib.auth.views import LogoutView


app_name = 'core'

urlpatterns = [
    path('login/', core.views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:login'), name='logout'),
    path('', core.views.Todo.index, name='todos'),
    path('doing/create', core.views.Todo.create, name='doing_create'),
    path('doing/<int:pk>/update/', core.views.TodoUpdate.as_view(), name='doing_update'),
    path('doing/<int:pk>/delete/', core.views.Todo.delete, name='doing_delete'),

]