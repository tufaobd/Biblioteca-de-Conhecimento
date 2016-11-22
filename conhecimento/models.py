from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Tema(models.Model):
    	tema = models.CharField(max_length=50)

    	def __str__(self):
    		return self.tema

class Publicacao(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	sinopse = models.TextField(max_length=200)	
	conteudo = models.TextField()
	data_publicacao = models.DateTimeField(default=timezone.now)
	tema = models.ManyToManyField(Tema, related_name='temas')

	objects = models.Manager()

	def publicacao(self):
		self.data_criacao = timezone.now()
		self.tema
		self.save()

	def __str__(self):
		return self.titulo


