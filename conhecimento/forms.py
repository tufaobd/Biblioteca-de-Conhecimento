from django import forms
from .models import Publicacao, Tema

class Aviso(forms.ModelForm):
	class Meta:
		model = Publicacao
		fields = ('titulo','sinopse','conteudo','tema',)
		
class Tema(forms.ModelForm):
	class Meta:
		model = Tema
		fields = ('tema',)
