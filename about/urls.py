from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_list, name="about_list"),
]
