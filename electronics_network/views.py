from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from electronics_network.models import Node
from electronics_network.paginators import NodePaginator
from electronics_network.serializers import NodeSerializer


class NodeListApiView(generics.ListAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    pagination_class = NodePaginator

    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ["contact__country", ]


class NodeCreateApiView(generics.CreateAPIView):
    serializer_class = NodeSerializer


class NodeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeUpdateApiView(generics.UpdateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeDestroyAPIView(generics.DestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
