from rest_framework import viewsets, filters
from .models import Produto, Categoria
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProdutoSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
  queryset = Produto.objects.all()
  serializer_class = ProdutoSerializer
  
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['preco', 'estoque','categoria__nome']  # Filtragem exata por preço e estoque
  search_fields = ['nome']  # Busca textual
  ordering_fields = ['nome', 'preco']  # Ordenação
  ordering = ['id']  # Ordenação padrão