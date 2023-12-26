from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from electronics_network.models import Node
from electronics_network.paginators import NodePaginator
from electronics_network.permission import IsActiveUser
from electronics_network.serializers import NodeSerializer, NodeCreateSerializer, NodeListSerializer


class NodeListApiView(generics.ListAPIView):
    """Вывод списка узлов с поставщиком"""
    queryset = Node.objects.all()
    serializer_class = NodeListSerializer
    pagination_class = NodePaginator
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["contact__country"]


class NodeCreateApiView(generics.CreateAPIView):
    """Создание узла с поставщиком"""
    serializer_class = NodeCreateSerializer
    permission_classes = [IsActiveUser]


class NodeRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр узла с поставщиком"""
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsActiveUser]


class NodeUpdateApiView(generics.UpdateAPIView):
    """Редактирование узла с поставщиком"""
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsActiveUser]


class NodeDestroyAPIView(generics.DestroyAPIView):
    """Удаление узла с поставщиком"""
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsActiveUser]
