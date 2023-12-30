from django.shortcuts import render, redirect
from .forms import SignUpForm

def SignUpComponent(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = SignUpForm()

    return render(
        request=request,
        template_name='Sign_up.html',
        context={'form': form}
    )
