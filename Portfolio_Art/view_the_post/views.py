from django.shortcuts import render

# Create your views here.
def ViewThePostComponent(request):
    return render(
        request, 
        "View_the_post.html", 
        {}
        )