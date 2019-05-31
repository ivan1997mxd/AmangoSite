from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogType


def blog_list(request):
    length = Blog.objects.all().count()
    context = {'blogs': Blog.objects.all(),
               'blogs_count': length,
               'blog_types': BlogType.objects.all()}
    return render(request, 'blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {'blog': get_object_or_404(Blog, pk=blog_pk)}
    return render(request, 'blog_detail.html', context)


def blog_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context = {'blogs': Blog.objects.filter(blog_type=blog_type),
               'blog_type': blog_type}
    return render(request, 'blogs_with_type.html', context)
