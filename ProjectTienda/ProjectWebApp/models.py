from tkinter import image_names
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    Titulo = models.CharField(max_length=150)
    Contenido = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='blog', null = True, blank = True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Pots'

    def __str__(self):
        return self.Titulo

