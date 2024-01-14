import json
from django.shortcuts import render, redirect
from .forms import PostForm
from core.models import Hashtag, Post

# Create your views here.
def UploadImageComponent(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        
        if post_form.is_valid():
            post_instance = post_form.save(commit=False)
            post_instance.user = request.user
            post_instance.save()
            
            hashtag_content = post_form.cleaned_data['hashtag']
            hashtags_list = hashtag_content.split()
            
            for hashtag in hashtags_list:
                Hashtag.objects.create(
                    post=post_instance, 
                    name_hashtag=hashtag.lower()
                    )

            return redirect('home')
        else :
             print(post_form.errors)
    else:
        post_form = PostForm()

    errors_json = json.dumps(post_form.errors)

    return render(
        request=request,
        template_name="Upload_image.html",
        context={
            'post_form': post_form,
            'errors_json': errors_json
                 }
    )

def EditPostComponent(request, post_id):
    post_to_edit = Post.objects.get(id=post_id)
    hashtag_to_post = Hashtag.objects.filter(post=post_to_edit)

    initial_hashtags = None

    if request.user == post_to_edit.user:
        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=post_to_edit)
            
            if post_form.is_valid():
                post_instance = post_form.save(commit=False)
                post_instance.user = request.user
                post_instance.save()

                for hashtag in hashtag_to_post:
                    hashtag.delete()
                
                hashtag_content = post_form.cleaned_data['hashtag']
                hashtags_list = hashtag_content.split()

                for hashtag in hashtags_list:
                    Hashtag.objects.create(
                        post=post_instance, 
                        name_hashtag=hashtag.lower()
                        )

            return redirect('home')
        else:
            post_form = PostForm(instance=post_to_edit)

            hashtag_name = [ hashtag.name_hashtag for hashtag in Hashtag.objects.filter(post__id= post_to_edit.id)]
            str_hashtags = " ".join(hashtag_name)

            post_form.fields['hashtag'].initial = str_hashtags

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