from django.shortcuts import render
from core.models import User
from .forms import NicknameForm, ImageUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def ConfigurationProfileComponent(request):
    user = User.objects.get(nickname=request.user.nickname)

    # Formulario para nombre de usuario
    form_nickname = NicknameForm(instance=request.user)
    if request.method == 'POST' and 'form_nickname' in request.POST:
        form_nickname = NicknameForm(request.POST, instance=request.user)
        if form_nickname.is_valid():
            form_nickname.save()
            messages.success(request, 'Nombre de usuario actualizado exitosamente.')
        else:
            messages.error(request, 'Error en el formulario de nombre de usuario.')

    # Formulario para imagen de usuario
    form_image = ImageUserForm(instance=request.user)
    if request.method == 'POST' and 'form_image' in request.POST:
        form_image = ImageUserForm(request.POST, instance=request.user)
        if form_image.is_valid():
            form_image.save()
            messages.success(request, 'Imagen de perfil actualizada exitosamente.')
        else:
            messages.error(request, 'Error en el formulario de imagen de perfil.')

    # Formulario para cambio de contraseña
    form_password = PasswordChangeForm(request.user)
    if request.method == 'POST' and 'form_password' in request.POST:
        form_password = PasswordChangeForm(request.user, request.POST)
        if form_password.is_valid():
            user = form_password.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión para evitar cerrar sesión
            messages.success(request, 'Contraseña actualizada exitosamente.')
        else:
            messages.error(request, 'Error en el formulario de cambio de contraseña.')

    return render(
        request=request,
        template_name="Configuration_profile.html",
        context={
            'user': user,
            'form_nickname': form_nickname,
            'form_image': form_image,
            'form_password': form_password
        }
    )