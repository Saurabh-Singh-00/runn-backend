from django.urls import path
from . import viewsets

urlpatterns = [
    path('', viewsets.UserViewSet.as_view({'post': 'create'}), name='user'),
    path('/detail/<str:email>', viewsets.UserViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('/stats', viewsets.UserStatsViewSet.as_view({'post': 'create'}), name='stats'),
    path('/stats/<str:email>', viewsets.UserStatsViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='stats'),
]