from django.shortcuts import render
from .models import Event


def about_list(request):
    context = {'events': Event.objects.all()}
    return render(request, 'about.html', context)


