from django.shortcuts import render
from . models import Produto, Pedido
def index(request):
    produtos = Produto.objects.all()


    context = {
        'produtos': produtos 
    }
    return render(request, "index.html", context)
