from django import views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Article
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


class BaseListView(ListView):
    template_name = 'NewsApp/home.html'
    queryset = Article.objects.order_by('-date')


def about(request):
    return render(request, 'NewsApp/about.html')


class ArticleListView(ListView):
    queryset = Article.objects.all().order_by('-date')
    template_name = 'NewsApp/home.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'NewsApp/news_detail.html'

    # def get_queryset(self, **kwargs):
    #     queryset = Article.objects.filter(category__slug=self.kwargs['slug'], status='published').order_by('-date')
    #     return queryset


class CategoryDetailView(ListView):
    template_name = 'NewsApp/category_detail.html'

    def get_queryset(self, **kwargs):
        queryset = Article.objects.filter(category__slug=self.kwargs['slug'], status='published').order_by('-date')
        return queryset
