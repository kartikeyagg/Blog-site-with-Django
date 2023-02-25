from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


# Create your views here.

def index(request):

    # return HttpResponse("Hello ")

    posts = Post.objects.all()

    params  ={
        'posts': posts,
    }


    return render(request,"index.html",params)


def post(request,pk):

    # print("tktr")

    posts = Post.objects.get(id=pk)

    param = {

        'posts': posts,

    }

    return render(request, 'post.html',param)