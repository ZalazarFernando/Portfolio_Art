from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Board, UserPost, comments
from .forms import BoardForm
from django.db.models import Q
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist

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

from django.http import HttpResponse

def LikePostComponent(request):
    try:
        if request.method == 'POST' and request.user.is_authenticated:
            post_id = request.POST.get('post_id')

            if post_id is not None:
                try:
                    post = Post.objects.get(id=post_id)
                    user_post, created = UserPost.objects.get_or_create(user=request.user, post=post)

                    if user_post.like:
                        user_post.like = False
                        post.likes -= 1
                    else:
                        user_post.like = True
                        post.likes += 1

                    user_post.save()
                    post.save()

                    return HttpResponse('success')
                except ObjectDoesNotExist:
                    return HttpResponse('error: Post does not exist')
            else:
                return HttpResponse('error: post_id is required')
        else:
            return HttpResponse('error: unauthorized')
    except Exception as e:
        print('Error:', str(e))
        return HttpResponse('error: ' + str(e))

def ProfileUserComponent(request):
    posting = Post.objects.filter(user=request.user)
    posting = posting.select_related('user').prefetch_related('hashtag_set')

    boards = Board.objects.filter(user=request.user)

    if request.user.is_authenticated:
        user = request.user

    context = {
        'posting' : posting,
        'boards' : boards,
        'user' : user
    }

    return render(
        request= request,
        template_name= "Profile_user.html",
        context= context
    )

def CreateNewBoardComponent(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('profile_user')
    else:
        form = BoardForm()

    return render(
        request= request,
        template_name= "Create_new_board.html",
        context= {'form' : form}
    )

def LogOutComponent(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")