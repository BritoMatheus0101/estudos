from django.contrib import admin
from . models import Produto, Pedido, InformacaoPedido
# Register your models here.

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(InformacaoPedido)