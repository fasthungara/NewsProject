from django.urls import path
from .views import MyHomeListView, by_rubric, details, NewsCreateView

app_name = 'newsblock'

urlpatterns = [
    path('', MyHomeListView.as_view(), name='list'),
    path('<int:id>/', by_rubric),
    path('<int:rubric_id>/<str:name>/', details, name='details'),
    path('create/',NewsCreateView.as_view(), name='create')
]