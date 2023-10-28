from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Advertisement, Rubric
from django.views.generic.edit import CreateView
from .forms import AdvertisementForm
from django.urls import reverse_lazy
# def index(request):
#     return render(request, 'ads_index.html')

class MyHomeTemplateView(TemplateView):
    template_name = 'ads_index.html'


class MyHomeListView(ListView):
    model = Advertisement
    template_name = 'ads_list.html'
    context_object_name = 'list'


class MyOwnCreateView(CreateView):
    form_class = AdvertisementForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')


def by_rubric(request, id):
    adv = Advertisement.objects.filter(rubric=id)

    rubric = Rubric.objects.get(id=id)
    context = {'adv': adv, 'rubric':rubric}
    return render(request, 'by_rubric.html', context=context)

def rubric(request):
    rubrics=Rubric.objects.all()
    context = {'rubrics':rubric}
    return render(request, 'rubrics.html', context=context)