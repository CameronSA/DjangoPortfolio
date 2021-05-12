from django.shortcuts import render

def cv_index(request):
    return render(request, "cv_index.html")