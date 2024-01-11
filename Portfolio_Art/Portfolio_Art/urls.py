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

from core.views import DeleteBoard, RemovePostComponent, DeletePostComponent, AddPostToBoardComponent, BoardComponent, LikePostComponent, HomeComponent, CreateNewBoardComponent, ViewThePostComponent, ProfileUserComponent, LogOutComponent
from log_in.views import LogInComponent
from sign_up.views import SignUpComponent
from upload_image.views import UploadImageComponent, EditPostComponent
from configuration_profile.views import ConfigurationProfileComponent

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('view_the_post/<int:post_id>/', ViewThePostComponent, name="view_the_post"),
    path('delete_post/', DeletePostComponent, name="delete_post"),
    path('remove_post_to_board/', RemovePostComponent, name="remove_post_to_board"),
    path('add_post_to_board/', AddPostToBoardComponent, name="add_post_to_board"),
    path('delete_board/', DeleteBoard, name="delete_board"),
    path('board/<int:board_id>/', BoardComponent, name="board"),
    path('like_post/', LikePostComponent, name="like_post"),
    path('log_in/', LogInComponent, name="log_in"),
    path('logout/', LogOutComponent, name="logout"),
    path('sign_up/', SignUpComponent, name="sign_up"),
    path('upload_image/', UploadImageComponent, name="upload_image"),
    path('edit_post/<int:post_id>/', EditPostComponent, name="edit_post"),
    path('profile_user/', ProfileUserComponent, name="profile_user"),
    path('create_new_board/', CreateNewBoardComponent, name="create_new_board"),
    path('configuration_profile/', ConfigurationProfileComponent, name="configuration_profile"),
    path('', HomeComponent, name="home"),
    path('<str:search>/', HomeComponent, name="home_with_param"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)