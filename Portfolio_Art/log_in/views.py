from django.shortcuts import render

# Create your views here.
def LogInComponent(request):
    return render(
        request, 
        "Log_in.html", 
        {}
        )