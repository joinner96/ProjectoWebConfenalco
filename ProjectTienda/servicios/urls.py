from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios, name="Servicios"),
    path('home', views.home, name="Home"),
    path('blog', views.blog, name="Blog"),
    path('tienda', views.tienda, name="Tienda"),
    path('contacto', views.contacto, name="Contacto"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)