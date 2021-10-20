from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

class Proposta(models.Model):
	nome = models.CharField(max_length=30)
	email = models.EmailField()
	celular = models.CharField(max_length=11)


class Perfil(models.Model):
	ESTADOS = (
        ('ACRE', 'AC'),
        ('ALAGOAS', 'AL'),
        ('AMAPÁ', 'AP'),
        ('AMAZONAS', ''),
        ('BAHIA', 'BA'),
        ('CEÁRA', 'CE'),
        ('DISTRITO FEDERAL', 'DF'),
        ('ESPÍRITO SANTO', 'ES'),
        ('GOÍAS', 'GO'),
        ('MARANHÃO', 'MA'),
        ('MATO GROSSO ', 'MT'),
        ('MATO GROSSO DO SUL', 'MINAS'),
        ('MINAS GERAIS', 'MG'),
        ('PARA', 'PA'),
        ('PARANÁ', 'PR'),
        ('PARAÍBA', 'PB'),
        ('PERNAMBUCO', 'PE'),
        ('PIAUÍ', 'PI'),
        ('RIO DE JANEIRO', 'RJ'),
        ('RIO GRANDE DO NORTE', 'RN'),
        ('RIO GRANDE DO SUL', 'RS'),
        ('RONDÔNIA', 'RO'),
        ('RORAIMA','RR'),
        ('SANTA CATARINA', 'SC'),
        ('SERGIPE', 'SE'),
        ('TOCANTINS', 'TO'),
    )
	nome = models.CharField(max_length=30)
	telefone = models.CharField(max_length=11)
	email = models.EmailField()
	Endereco = models.CharField(max_length=50)
	numero = models.CharField(max_length=5)
	complemento = models.CharField(max_length=25)
	cidade = models.CharField(max_length=30)
	estado =models.CharField(max_length=22,choices=ESTADOS)
	bairro = models.CharField(max_length=30)
	creci = models.CharField(max_length=6)
	estado_creci = models.CharField(max_length=22,choices=ESTADOS)
	
class Imagens(models.Model):
	imagem_perfil = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
	imagem_capa = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
	imagem_formulario = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
    

class Anuncio (models.Model):
	NEGOCIACAO = (
		('VENDA','VENDA'),
		('ALUGA','ALUGA'),
		('COMPRA','COMPRA'),
		)

	STATUS = (
		('LANÇAMENTO','LANÇAMENTO'),
		('EM OBRAS','EM OBRAS'),
		('PRONTO PARA MORAR','PRONTO PARA MORAR'),
		)

	TIPO = (
		('APARTAMENTO','APARTAMENTO'),
		('CASA','CASA'),
		('TERRENO','TERRENO'),
		('COMERCIAL','COMERCIAL'),
		('GALPÃO','GALPÃO'),
		('CHACARÁ','CHACARÁ'),
		('SÍTIO','SÍTIO'),
		('FAZENDA','FAZENDA'),
		)
	

	negociacao = models.CharField(max_length=6, choices=NEGOCIACAO)
	status = models.CharField(max_length=18,choices=STATUS)
	tipo_imovel = models.CharField(max_length=12, choices=TIPO)
	titulo_anuncio = models.CharField(max_length=30)
	bairro = models.CharField(max_length=30)
	endereco =models.CharField(max_length=30)
	descricao = models.TextField(max_length=150)
	imagem1 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
	imagem2 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
	imagem3 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
	imagem4 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
	imagem5 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=False)
	imagem6 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=False,blank=True)
	imagem7 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=True,blank=True)
	imagem8 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=True,blank=True)
	imagem9 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG',null=True,blank=True)
	imagem10 = ResizedImageField(size=[660, 540], quality=100, upload_to='media/',force_format='PNG', null=True,blank=True)
	anunciado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


