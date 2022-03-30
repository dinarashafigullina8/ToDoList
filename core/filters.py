import django_filters

import core.models


class DoingFilter(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='icontains', label='Название')

    class Meta:
        model = core.models.Doing
        fields = '__all__'
