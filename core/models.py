from django.db import models


class Doing(models.Model):
    name = models.CharField('Список дел', max_length=128)
    completed = models.BooleanField('Выполнено?', default=False)

    def __str__(self):
        return self.name
