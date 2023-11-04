from django.shortcuts import render
from .models import News, Rubric
from django.views.generic import ListView, CreateView
from .forms import NewsForm
from django.urls import reverse_lazy

def by_rubric(request, id):
    news = News.objects.filter(rubric=id)

    rubric = Rubric.objects.get(id=id)
    context = {'news': news, 'rubric':rubric}
    return render(request, 'by_rubric.html', context=context)

class MyHomeListView(ListView):
    model = News
    template_name = 'main.html'
    context_object_name = 'list'

def details(request, rubric_id, name):
    new = News.objects.filter(title=name, rubric=rubric_id).first()

    context = {'rubric': new.rubric, 'new': new}
    return render(request, 'details.html', context=context)

class NewsCreateView(CreateView):
    form_class = NewsForm
    template_name = 'create.html'
    success_url = reverse_lazy('newsblock:list')