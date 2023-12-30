from django.shortcuts import render

# Create your views here.
def UploadImageComponent(request):

    return render(
        request= request,
        template_name= "Upload_image.html",
        context= {}
    )