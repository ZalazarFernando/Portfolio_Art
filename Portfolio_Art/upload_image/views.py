from django.shortcuts import render, redirect
from .forms import PostForm, HashtagForm
from core.models import Hashtag

# Create your views here.
def UploadImageComponent(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        hashtag_content = request.POST.get('hashtag')
        #hashtag_form = HashtagForm(request.POST)
        if post_form.is_valid() and hashtag_content is not None:
            post_instance = post_form.save(commit=False)
            post_instance.user = request.user
            post_instance.save()

            """hashtag_instance = hashtag_form.save(commit=False)
            hashtag_instance.post_id = post_instance.id
            hashtag_instance.save()"""
            
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