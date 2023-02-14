from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tovaru', views.about, name='tovaru'),
    path('reg', views.reg, name='reg')
]
