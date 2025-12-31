from django.urls import path
from .views import *
urlpatterns = [
    path('register/', register_view, name='register'),
    path('success/', success_view, name='success_view')
]
