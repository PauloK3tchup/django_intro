from rest_framework import viewsets, filters
from .models import Produto, Categoria
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProdutoSerializer, CategoriaSerializer
from .filters import ProdutoFilter

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
  queryset = Produto.objects.all()
  serializer_class = ProdutoSerializer
  
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  
  filterset_fields = {
    'estoque': ['exact', 'gte', 'lte'],  # permite filtro exato, maior ou igual e menor ou igual
  }  
  search_fields = ['nome']  # Busca textual
  ordering_fields = ['nome', 'preco']  # Ordenação
  ordering = ['id']  # Ordenação padrão