import django_filters
from django.forms import DateInput
from django_filters import FilterSet, ModelMultipleChoiceFilter, CharFilter, DateTimeFilter
from .models import Post, PostCategory, Category


class NewsFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Категория'
    )
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название'
    )

    dateCreation = DateTimeFilter(
            field_name='dateCreation',
            label='Новости до',
            lookup_expr='gt',
            widget=DateInput(
                format="%Y-%m-%d %H:%M",
                attrs={'type': 'datetime-local'},
            ),
        )