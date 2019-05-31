from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list, name="case_list"),
]
