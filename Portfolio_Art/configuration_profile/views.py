from django.shortcuts import render

# Create your views here.
def ConfigurationProfileComponent(request):

    return render(
        request= request,
        template_name= "Configuration_profile.html",
        context= {}
    )