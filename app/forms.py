from django import forms
from .models import Proposta, Perfil, Anuncio

class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = '__all__'

class PerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = '__all__'

class AnuncioForm(forms.ModelForm):
	class Meta:
		model = Anuncio
		fields = (
			'negociacao',
			'status',
			'tipo_imovel',
			'titulo_anuncio',
			'bairro',
			'endereco',
			'descricao',
			'imagem1',
			'imagem2',
			'imagem3',
			'imagem4',
			'imagem5',
			'imagem6',
			'imagem7',
			'imagem8',
			'imagem9',
			'imagem10',
			
			)



