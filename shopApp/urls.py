from django.urls import path
from shopApp.views import index, about  

urlpatterns = [
    path('', index),
    path('about/', about, name = 'about')
]