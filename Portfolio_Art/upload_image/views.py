from django.shortcuts import render, redirect
from .forms import PostForm, HashtagForm
from core.models import Hashtag, Post

# Create your views here.
def UploadImageComponent(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        hashtag_content = request.POST.get('hashtag')

        if post_form.is_valid() and hashtag_content is not None:
            post_instance = post_form.save(commit=False)
            post_instance.user = request.user
            post_instance.save()
            
            hashtags_list = hashtag_content.split()

            for hashtag in hashtags_list:
                Hashtag.objects.create(
                    post=post_instance, 
                    name_hashtag=hashtag
                    )

            return redirect('home')
    else:
        post_form = PostForm()
        #hashtag_form = HashtagForm()

    return render(
        request=request,
        template_name="Upload_image.html",
        context={'post_form': post_form}
    )

def EditPostComponent(request, post_id):
    post_to_edit = Post.objects.get(id=post_id)
    hashtag_to_post = Hashtag.objects.filter(post=post_to_edit)

    initial_hashtags = None

    if request.user == post_to_edit.user:
        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=post_to_edit)
            hashtag_content = request.POST.get('hashtag')
            
            if post_form.is_valid() and hashtag_content is not None:
                post_instance = post_form.save(commit=False)
                post_instance.user = request.user
                post_instance.save()

                for hashtag in hashtag_to_post:
                    hashtag.delete()
                
                hashtags_list = hashtag_content.split()

                for hashtag in hashtags_list:
                    Hashtag.objects.create(
                        post=post_instance, 
                        name_hashtag=hashtag
                        )

            return redirect('home')
        else:
            post_form = PostForm(instance=post_to_edit)

            initial_hashtags = ' '.join(hashtag.name_hashtag for hashtag in hashtag_to_post)

    else:
        return redirect('home')

    return render(
        request=request,
        template_name="Upload_image.html",
        context={
            'post_form': post_form,
            'initial_hashtags' : initial_hashtags
            }
    )