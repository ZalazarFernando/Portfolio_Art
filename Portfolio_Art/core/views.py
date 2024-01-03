from django.shortcuts import render
from .models import Post, Board, UserBoard
from django.db.models import Q

# Create your views here.
def HomeComponent(request, search=None):
    if search:
        posting = Post.objects.filter(Q(title__icontains=search) | Q(hashtag__name_hashtag__icontains=search))
    else:
        posting = Post.objects.select_related('user').prefetch_related('hashtag_set').all()

    posting = posting.select_related('user').prefetch_related('hashtag_set')

    context = {
        'posting' : posting
    }

    return render(
        request= request, 
        template_name="Home.html", 
        context= context
        )

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

def ProfileUserComponent(request):
    posting = Post.objects.filter(user=request.user)
    posting = posting.select_related('user').prefetch_related('hashtag_set')

    id_board = UserBoard.objects.filter(user=request.user)
    boards = Board.objects.filter(id__in=id_board.values('board'))

    context = {
        'posting' : posting,
        'boards' : boards
    }

    return render(
        request= request,
        template_name= 'Profile_user.html',
        context= context
    )