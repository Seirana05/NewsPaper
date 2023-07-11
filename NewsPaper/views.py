from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy
from .forms import PostForm
from .filters import NewsFilter
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


# def news_search(request):
#     queryset = Post.objects.all()
#     filterset = NewsFilter(request.GET, queryset)
#
#     context = {
#         'filterset': filterset,
#         'news_search': filterset.qs,
#     }
#     return render(request, 'search.html', context)


class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class Search(NewsList):
    template_name = 'search.html'
    context_object_name = 'news_search'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['something'] = 'some'
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class NewsCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/articles/create/':
            post.categoryType = 'AR'
        elif self.request.path == '/news/news/create/':
            post.categoryType = 'NW'
        post.save()  # сохраняем изменения в базу данных
        return super().form_valid(form)

    success_url = reverse_lazy('news_list')

class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


