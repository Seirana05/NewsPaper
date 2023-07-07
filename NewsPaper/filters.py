import django_filters
from django_filters import FilterSet, ModelMultipleChoiceFilter, CharFilter
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