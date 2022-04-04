# Generated by Django 4.0.3 on 2022-04-04 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_remove_doing_date_doing_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doing',
            options={'verbose_name': 'Дело', 'verbose_name_plural': 'Дела'},
        ),
        migrations.AddField(
            model_name='doing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='doing',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название задачи'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='doing',
            order_with_respect_to='user',
        ),
    ]