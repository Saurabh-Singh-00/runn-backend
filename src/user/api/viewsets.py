from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from . import serializers


class UserViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        user = super().create(request, *args, **kwargs)
        serializers.model.UserStats.create(email=user.data['email'])
        return user

    def retrieve(self, request, email=None):
        user = get_object_or_404(serializers.model.User, email=email)
        return Response(serializers.UserSerializer(user).data)


class UserStatsViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):

    serializer_class = serializers.UserStatsSerializer

    def update(self, request, **kwargs):
        try:
            stats = get_object_or_404(serializers.model.UserStats, email=kwargs.pop('email'))
            stats.steps += int(request.data['steps'])
            stats.distance += int(request.data['distance'])
            stats.save()
        except Http404 as e:
            return Response(exception=e)
        return Response(serializers.UserStatsSerializer(stats).data)

    def retrieve(self, request, email=None):
        stats = get_object_or_404(serializers.model.UserStats, email=email)
        return Response(serializers.UserStatsSerializer(stats).data)

class UserStatsByMarathonViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.UserStatsByMarathonSerializer

    def get_queryset(self, *args, **kwargs):
        return serializers.model.UserStatsByMarathon.objects.filter(marathon_id=self.kwargs['marathon_id'], email=self.kwargs['email'])