from django.shortcuts import render, HttpResponse
from ProjectWebApp.models import Post
# Create your views here.
def home(request):

    return render(request, "ProjectWebApp/home.html")

def blog(request):
    posts = Post.objects.all()
    return render(request, "ProjectWebApp/blog.html", {"posts": posts})

def tienda(request):

    return render(request, "ProjectWebApp/tienda.html")



def contacto(request):

    return render(request, "ProjectWebApp/contacto.html")