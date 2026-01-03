from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import json

# Create your views here.
def home(request):
    return render(request, 'index.html', {"data": Post.objects.all().order_by('createdAt')})

def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'createPost.html', {'form': "recieved"})