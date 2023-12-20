from django.urls import path

from electronics_network.apps import ElectronicsNetworkConfig
from electronics_network.views import NodeListApiView, NodeCreateApiView, NodeUpdateApiView, NodeDestroyAPIView, \
    NodeRetrieveAPIView

app_name = ElectronicsNetworkConfig.name

urlpatterns = [
    path('', NodeListApiView.as_view(), name='node-list'),
    path('create/', NodeCreateApiView.as_view(), name='node-create'),
    path('update/<int:pk>', NodeUpdateApiView.as_view(), name='node-update'),
    path('delete/<int:pk>/', NodeDestroyAPIView.as_view(), name='node-delete'),
    path('<int:pk>/', NodeRetrieveAPIView.as_view(), name='node-view'),
]
