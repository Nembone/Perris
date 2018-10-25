from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Usuario
from .forms import RegistroForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts' : posts})


def registroUsuario(request):
	### *** inicio: se incluye las variables para que sean agregados al formulario o vista html
	form = RegistroForm(request.POST or None) ## clase declarada en forms.py
	### *** fin

	print ("Este mensaje aparece en la consola donde esta ejectandose el comando runserver")
	# print(dir(form)) # funciones disponible con el form

	# captura de los datos que fueron enviados por el usuario con el metodo POST
	# se valida para no tener error de lectura de datos
	if form.is_valid():
		datos = form.cleaned_data
		print (datos.get("nombre"))
		print (datos.get("mascota"))
		print (datos.get("email"))

		# se guarda en la bdd
		nombre = datos.get("nombre")
		email = datos.get("email")
		mascota = datos.get("mascota")
		
		objetoUsuario = Usuario()
		objetoUsuario.nombre = nombre
		objetoUsuario.email = email
		objetoUsuario.mascota = mascota
		objetoUsuario.save()


	### *** inicio: se incluye en la linea de abajo, las variables declaradas en el archivo forms.py
	contexto = {"formulario" : form}
	## en la clase regitroUsuario
	### *** fin
	return render(request, "inicio.html", contexto)

### 
### Crear archivo forms.py en la raiz del proyecto y su contenido
### despues agregar los codigos señalado con ***