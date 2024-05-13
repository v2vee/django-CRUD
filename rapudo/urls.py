from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name='test'),
    path('insert-products/', views.insertProducts, name='insert-products'),
]
