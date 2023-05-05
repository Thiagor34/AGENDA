from django.db import models

# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.IntegerField()
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    descricao = models.TextField()
    data_nascimento = models.DateField()
    ativo = models.BooleanField()
    
    def __str__(self) -> str:
        return self.nome
    
    class Meta: 
        verbose_name_plural = 'Contatos'

