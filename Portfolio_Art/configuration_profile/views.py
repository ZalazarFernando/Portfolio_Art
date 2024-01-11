from django.shortcuts import render
from core.models import User
from .forms import NicknameForm, ImageUserForm
from django.contrib import messages

# Create your views here.
def ConfigurationProfileComponent(request):
    user = User.objects.get(nickname= request.user.nickname)

    # formulario para nombre de usuario
    if request.method == 'POST':
        form_nickname = NicknameForm(request.POST, instance=request.user)

        if form_nickname.is_valid():
            form_nickname.save()
        else:
            print("error: formulario invalido")
    else :
        form_nickname = NicknameForm(instance=request.user)

    # formulario para imagen de usuario
    if request.method == 'POST':
        form_image = ImageUserForm(request.POST, instance= request.user)

        if form_image.is_valid():
            form_image.save()
        else:
            print("error: formulario invalido")
    else:
        form_image = ImageUserForm(instance=request.user)

    return render(
        request= request,
        template_name= "Configuration_profile.html",
        context= {
            'user' : user,
            'form_nickname' : form_nickname,
            'form_image' : form_image
        }
    )