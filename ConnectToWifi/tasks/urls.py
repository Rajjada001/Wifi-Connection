from django.urls import path
from . import views
#Create urls

urlpatterns = [
    path('', views.home, name='home'),
    path('form_res/',views.res, name='form_res'),
]