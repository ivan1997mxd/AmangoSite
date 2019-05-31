from django.shortcuts import render
from .models import Contact


def contact_list(request):
    context = {'contacts': Contact.objects.all()}
    return render(request, 'contact.html', context)
