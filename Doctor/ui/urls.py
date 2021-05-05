from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='home'),
    path('about/', index, name='about'),
    path('contact/', index, name='contact'),
    path('blog1/', index, name='blog'),
    path('blog/', index, name='blog'),
    path('services/', index, name='services'),
]
