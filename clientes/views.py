from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["nome"]
    ordering_fields = ["nome"]
    filterset_fields = ["ativo"]
