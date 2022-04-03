from django.db import models


class Doing(models.Model):
    name = models.CharField('Название задачи', max_length=128)
    completed = models.BooleanField('Выполнено?', default=False)

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'

    def __str__(self):
        return self.name
