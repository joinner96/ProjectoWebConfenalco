from django.shortcuts import render
from servicios.models import servicio
# Create your views here.

def servicios(request):
    servicios=servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})


#provicional :c
def home(request):

    return render(request, "ProjectWebApp/home.html")

def blog(request):

    return render(request, "ProjectWebApp/blog.html")

def tienda(request):

    return render(request, "ProjectWebApp/tienda.html")



def contacto(request):

    return render(request, "ProjectWebApp/contacto.html")