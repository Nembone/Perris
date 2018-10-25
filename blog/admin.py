from django.contrib import admin
from .models import Post
from .models import Usuario, Mascota

# se especifica que mostrar en el listado del CRUD de usuario
# dado que por defecto muestra el contenido de la funcion
# def __str__(self): de la clase en models.py
class AdminUsuario(admin.ModelAdmin):
    list_display = ["nombre", "email"]
    class Meta:
        model = Usuario
    

admin.site.register(Post)
# original o primera vista

admin.site.register(Usuario, AdminUsuario)
admin.site.register(Mascota)