from django.urls import path
from . import viewsets

urlpatterns = [
    path('', viewsets.MarathonViewSet.as_view({'get': 'list', 'post': 'create'}), name='marathon'),
    path('/<str:country>/<uuid:id>/detail', viewsets.MarathonViewSet.as_view({'get': 'retrieve'}), name='marathon-detail'),
    path('/<uuid:marathon_id>/runner', viewsets.RunnerViewSet.as_view({'get': 'list'}), name='runner'),
    path('/<uuid:marathon_id>/participate', viewsets.RunnerViewSet.as_view({'post': 'create'}), name='runner'),
    path('/runner/<str:user_email>', viewsets.MarathonByRunnerViewSet.as_view({'get': 'list', 'post': 'create'}), name='marathon-by-runner'),
    path('/sponsor/<str:sponsor_id>', viewsets.MarathonBySponsorViewSet.as_view({'get': 'list', 'post': 'create'}), name='marathon-by-sponsor')
]