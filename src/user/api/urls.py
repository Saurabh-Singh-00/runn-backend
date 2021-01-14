from django.urls import path
from . import viewsets

urlpatterns = [
    path('', viewsets.UserViewSet.as_view({'post': 'create'}), name='user'),
    path('/detail/<str:email>', viewsets.UserViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('/stats', viewsets.UserStatsViewSet.as_view({'post': 'create'}), name='stats'),
    path('/stats/<str:email>', viewsets.UserStatsViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='stats'),
    path('/stats/<uuid:marathon_id>/<str:email>', viewsets.UserStatsByMarathonViewSet.as_view({'get': 'list', 'post': 'create'}), name='stats-by-marathon'),
    path('/stats/<uuid:marathon_id>/<str:email>/complete', viewsets.UserStatsByMarathonViewSet.as_view({'get': 'check_completion'}), name='marathon-completion'),
]