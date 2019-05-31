"""AmangoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from index import views

admin.site.site_title = '艾满高后台'
admin.site.site_header = '艾满高网站管理后台'

urlpatterns = [
    path('', views.info_list, name="info_list"),
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('about/', include('about.urls')),
    path('case/', include('case.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
]
