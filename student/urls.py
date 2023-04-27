from django.urls import path
from . import views

app_name='student'


urlpatterns = [
    path('studentlogin', views.studentlogin,name='studentlogin'),
    path('studentview', views.studentview,name='studentview'),
    path('masterstu', views.masterstu,name='masterstu'),
]
