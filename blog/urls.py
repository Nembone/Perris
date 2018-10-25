from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^RegistroUsuario/$', views.registroUsuario, name='RegistroUsuario'),
	url(r'^RegistroUsuario/$', views.registroUsuario, name='RegistroUsuario'),
]
