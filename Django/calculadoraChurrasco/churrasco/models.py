from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField("Nome", max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

class Pedido (models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank = True, null = True)
    quantidade = models.DecimalField("Quantidade",decimal_places=2, max_digits=9)
    preco = models.DecimalField("Preço médio",decimal_places=2, max_digits=9)
    cidade = models.CharField("Cidade", max_length=500)