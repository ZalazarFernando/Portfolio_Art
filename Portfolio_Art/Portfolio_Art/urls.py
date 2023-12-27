"""
URL configuration for Portfolio_Art project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import HomeComponent
from view_the_post.views import ViewThePostComponent
from log_in.views import LogInComponent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeComponent, name="home"),
    path("view_the_post/", ViewThePostComponent, name="view_the_post"),
    path('log_in/', LogInComponent, name="log_in")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
