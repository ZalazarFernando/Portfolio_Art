from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Post, Board, UserPost, Comments, BoardPost, User
from .forms import BoardForm, CommentForm
from django.db.models import Q
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

# Create your views here.
def HeaderBarComponent(request):
    user = User.objects.get(nickname= request.user.nickname)

    return render(
        request= request,
        template_name= "Header_bar.html",
        context= {
            'user' : user
        }
    )

def HomeComponent(request, search=None):
    if search:
        posting = Post.objects.filter(Q(title__icontains=search) | Q(hashtag__name_hashtag__icontains=search))
        boards = Board.objects.filter(name__icontains=search)
    else:
        posting = Post.objects.select_related('user').prefetch_related('hashtag_set').all()
        boards = None

    posting = posting.select_related('user').prefetch_related('hashtag_set')

    context = {
        'posting' : posting.order_by('-likes'),
        'boards' : boards
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

    if request.user.is_authenticated:
        boards = Board.objects.filter(user= request.user)
    else:
        boards = 0

    # elementos ocultos para mostrar comentarios
    user_post_comments = Comments.objects.filter(post__post=post_id)

    comments_to_show = [{'user': comment.post.user.nickname, 'comment': comment.comment} for comment in user_post_comments]


    # formulario oculto para nuevos comentarios
    num_comments = 0

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            
            user_post, created = UserPost.objects.get_or_create(
                user=request.user, 
                post=Post.objects.get(id=request.POST.get('post_id'))
            )

            new_comment = form.save(commit=False)
            new_comment.post = user_post
            new_comment.save()

            user_post = UserPost.objects.get(user=request.user, post=posting)

            return HttpResponseRedirect(request.path_info)
        else:
            print(form.errors)
    else:
        form = CommentForm()

    num_comments = Comments.objects.filter(
        post__post= post_id
        ).count()

    context = {
        'posting' : posting,
        'hashtags' : hashtags,
        'all_posting' : all_posting,
        'num_comments' : str(num_comments),
        'comments_to_show' : comments_to_show,
        'boards' : boards,
        'form' : form
    }

    return render(
        request= request, 
        template_name= "View_the_post.html", 
        context= context
        )

def DeletePostComponent(request):
    try:
        if request.method == 'POST' and request.user.is_authenticated:
            post_id = request.POST.get('post_id')

            if post_id is not None:
                try:
                    Post.objects.get(id=post_id).delete()
                    return HttpResponse('success')
                except ObjectDoesNotExist:
                    return HttpResponse('error: ObjectDoesNotExist')
            else:
                return HttpResponse('error: post_id is required')
        else:
            return HttpResponse('error: unauthorized')
    except Exception as e:
        print('Error:', str(e))
        return HttpResponse('error: ' + str(e))
    
def RemovePostComponent(request):
    try:
        if request.method == 'POST' and request.user.is_authenticated:
            post_id = request.POST.get('post_id')
            board_id = request.POST.get('board_id')

            if post_id is not None and board_id is not None:
                try:
                    BoardPost.objects.get(
                        board= board_id,
                        post= post_id
                        ).delete()

                    return HttpResponse("success")
                except ObjectDoesNotExist:
                    return HttpResponse('error: ObjectDoesNotExist')
            else:
                return HttpResponse('error: post_id is required')
        else:
            return HttpResponse('error: unauthorized')
    except Exception as e:
        print('Error:', str(e))
        return HttpResponse('error: ' + str(e))
    

def LikePostComponent(request):
    try:
        if request.method == 'POST' and request.user.is_authenticated:
            post_id = request.POST.get('post_id')

            if post_id is not None:
                try:
                    post = Post.objects.get(id=post_id)
                    user_post, created = UserPost.objects.get_or_create(user=request.user, post=post)

                    if not created:
                        user_post.like = not user_post.like
                    else:
                        user_post.like = True

                    if user_post.like:
                        post.likes += 1
                    else:
                        post.likes -= 1

                    post.save()
                    user_post.save()

                    return HttpResponse('success')
                except ObjectDoesNotExist:
                    return HttpResponse('error: ObjectDoesNotExist')
            else:
                return HttpResponse('error: post_id is required')
        else:
            return HttpResponse('error: unauthorized')
    except Exception as e:
        print('Error:', str(e))
        return HttpResponse('error: ' + str(e))
    
def AddPostToBoardComponent(request):
    if request.method == 'POST' and request.user.is_authenticated:
        board_id = request.POST.get('board_id')
        post_id = request.POST.get('post_id')

        if board_id and post_id:
            try:
                board = Board.objects.get(id=board_id)
                post = Post.objects.get(id=post_id)

                BoardPost.objects.create(board=board, post=post)

                return HttpResponse('success')
            except (Board.DoesNotExist, Post.DoesNotExist):
                return HttpResponse('error: Board or Post does not exist')
        else:
            return HttpResponse('error: board_id and post_id are required')
    else:
        return HttpResponse('error: unauthorized')

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

def BoardComponent(request, board_id):
    boards = Board.objects.filter(user= request.user)
    board = Board.objects.get(id=board_id)
    board_posts = BoardPost.objects.filter(board = board.id)

    posts_of_board = [board_post.post for board_post in board_posts]
    context = {
            'board' : board,
            'boards' : boards,
            'posts_of_board' : posts_of_board
        }

    return render(
        request= request,
        template_name= "Board.html",
        context= context
    )

def DeleteBoard(request):
    
    try:
        if request.method == 'POST' and request.user.is_authenticated:
            
            board_id = request.POST.get('board_id')

            if board_id is not None:
                try:
                    Board.objects.get(id= board_id).delete()
                    
                    return HttpResponse('success')
                except (Board.DoesNotExist, Post.DoesNotExist):
                    return HttpResponse('error: Board or Post does not exist')
            else:
                return HttpResponse('error: board_id and post_id are required')
        else:
            return HttpResponse('error: unauthorized')
    except Exception as e:
        print('Error:', str(e))
        return HttpResponse('error: ' + str(e))

def LogOutComponent(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")