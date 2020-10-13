from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.AddImageView.as_view(), name='create'),
    path('search/', views.Search.as_view(), name='search')
]
