from django.shortcuts import render

# Create your views here.
def HomeComponent(request):
    return render(
        request, 
        "Home.html", 
        {}
        )