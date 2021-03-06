from django.contrib.auth.models import User
from django.db import models


class Doing(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Название задачи', max_length=128)
    completed = models.BooleanField('Выполнено?', default=False)

    class Meta:
        order_with_respect_to = 'user'
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'

    def __str__(self):
        return self.name
