from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    pass
    #return HttpResponse('Hello Posts')
    return render(request, 'posts/index.html',{'title':'Latest Post'})
