from django.urls import path
from .views import MyHomeTemplateView, MyHomeListView, MyOwnCreateView, by_rubric

app_name='Advertisements'

urlpatterns = [
    path('', MyHomeTemplateView.as_view(),name='index'),
    path('list/', MyHomeListView.as_view(), name='list'),
    path('create/',MyOwnCreateView.as_view(), name='create'),
    path('<int:id>/', by_rubric),
]