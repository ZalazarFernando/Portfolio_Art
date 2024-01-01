from django.shortcuts import render, redirect
from .forms import PostForm, HashtagForm

# Create your views here.
def UploadImageComponent(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        hashtag_form = HashtagForm(request.POST)
        if post_form.is_valid() and hashtag_form.is_valid():
            post_instance = post_form.save(commit=False)
            post_instance.user = request.user  # Asignar el id del usuario actual
            post_instance.save()

            hashtag_instance = hashtag_form.save(commit=False)
            hashtag_instance.post_id = post_instance.id
            hashtag_instance.save()

            return redirect('home')
    else:
        post_form = PostForm()
        hashtag_form = HashtagForm()

    return render(
        request=request,
        template_name="Upload_image.html",
        context={'post_form': post_form, 'hashtag_form': hashtag_form}
    )