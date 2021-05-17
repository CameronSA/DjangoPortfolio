from django.shortcuts import render
from home_page.models import ProfilePicture

def home_index(request):
    image = ProfilePicture.objects.all()[0]
    context = {
        "image": image,
    }
    return render(request, "home_index.html", context)