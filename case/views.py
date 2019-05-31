from django.shortcuts import render
from .models import Case


def case_list(request):
    context = {'cases': Case.objects.all()}
    return render(request, 'case.html', context)
