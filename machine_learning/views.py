from django.shortcuts import render

def machine_learning_index(request):
    return render(request, "machine_learning_index.html")

def supervised_learning_index(request):
    return render(request, "supervised_learning_index.html")

def unsupervised_learning_index(request):
    return render(request, "unsupervised_learning_index.html")

