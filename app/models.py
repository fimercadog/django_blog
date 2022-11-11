from django.db import models


# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100)
    estado = models.BooleanField('Categoria Activada//Categoria no activada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Autor', max_length=255)
    apellidos = models.CharField('Appelidos del autor', max_length=255)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Github', null=True, blank=True)
    correo=models.EmailField('Correo Electronico')
    estado=models.BooleanField('Autor Activo/NO Activo',default=True)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return  "{0},{1}".format(self.apellidos,self.nombre)
