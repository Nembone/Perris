from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Usuario(models.Model):
    nombre = models.CharField(max_length=35)
    email = models.EmailField()
    nombre_mascota = models.CharField(max_length=35)
    SEXOS = (('H', 'Hembra'), ('M', 'Macho'))
    Sexo_mascota = models.CharField(max_length=1, choices=SEXOS, default='H')
    fecha_registro = models.DateField(
            auto_now=True)

    def __str__(self):
        self.save()
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=35)
    nombre_mascota = models.CharField(max_length=35)
    SEXOS = (('H', 'Hembra'), ('M', 'Macho'))
    Sexo_mascota = models.CharField(max_length=1, choices=SEXOS, default='H')
    fecha_nacimiento_mascota = models.DateTimeField()
    
    def __str__(self):
        self.save()
        return self.nombre_mascota



# por cada modelo agregado, se debe ejecutar para agregar
# python manage.py makemigrations y despues
# python manage.py migrate
# Despues en admin.py agregar:
#  from .models import Usuario
# y despues:
#  admin.site.register(Usuario)
# ver la administracion de la pagina en el archivo admin.py