from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.Doings.index, name='index'),
    path('doing/create/', core.views.DoingCreate.as_view(), name='doing_create'),
    path('doing/update', core.views.DoingUpdate.as_view(), name='doing_update'),
    path('doing/delete', core.views.DoingDelete.as_view(), name='doing_delete'),

]