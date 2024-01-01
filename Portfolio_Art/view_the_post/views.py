from django.shortcuts import render
from core.models import Post

# Create your views here.
def ViewThePostComponent(request, post_id):
    all_posting = Post.objects.select_related('user').prefetch_related('hashtag_set').all()

    posting = Post.objects.get(id=post_id)
    hashtags = posting.hashtag_set.all()

    context = {
        'posting' : posting,
        'hashtags' : hashtags,
        'all_posting' : all_posting
    }

    return render(
        request= request, 
        template_name= "View_the_post.html", 
        context= context
        )