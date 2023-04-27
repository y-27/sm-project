from django.urls import path
from . import views

app_name='schooladmin'

urlpatterns = [
     path('pages', views.pages,name='pages'),
     
]