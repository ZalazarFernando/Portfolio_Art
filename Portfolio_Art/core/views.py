from django.shortcuts import render
from .models import User, Post, Hashtag

# Create your views here.
def HomeComponent(request):
    posting = Post.objects.select_related('user_id').prefetch_related('hashtag_set').all()


    context = {
        'posting' : posting
    }

    return render(
        request= request, 
        template_name="Home.html", 
        context= context
        )