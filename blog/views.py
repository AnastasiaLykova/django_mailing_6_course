import random

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import ArticleForm
from blog.models import Blog
from clients.models import Clients
from mailing.models import Mailing


class ArticleListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}



class ArticleDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Статья'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counts += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Blog
    form_class = ArticleForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        new_art = form.save()
        new_art.slug = slugify(new_art.title)
        new_art.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Blog
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('blog:article', args=[self.object.pk])


class ArticleDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class GeneralView(ListView):
    model = Blog
    template_name = 'blog/general.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailings = len(Mailing.objects.all())
        mailings_is_active = len(Mailing.objects.filter(status='started'))
        unique_clients_count = Clients.objects.values('email').count()
        context['mailings'] = mailings
        context['mailings_is_active'] = mailings_is_active
        context['unique_clients_count'] = unique_clients_count
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:3]
