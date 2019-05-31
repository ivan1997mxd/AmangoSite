from django.shortcuts import render, get_object_or_404
from .models import Info


def info_list(request):
    context = {'infos': Info.objects.all()}
    return render(request, 'home.html', context)


