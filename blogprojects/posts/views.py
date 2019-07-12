from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10] #Post objects fetch and frist 10 post fetch
    context = {
        'title':'Latest Post',
        'posts': posts,
    }
    #return HttpResponse('Hello Posts')
    return render(request, 'posts/index.html',context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context ={
        'post': post,
    }

    return render(request,'posts/details.html', context)