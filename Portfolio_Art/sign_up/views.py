from django.shortcuts import render

# Create your views here.
def SignUpComponent(request):
    return render(
        request, 
        "Sign_up.html", 
        {}
        )