from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404
import json
from . import serializers


class UserViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.UserSerializer

    def serialize_user(self, user):
        return {
            "email": user.email,
            "dob": str(user.dob),
            "name": user.name,
            "pic": user.pic
        }

    def create(self, request, *args, **kwargs):
        user = serializers.model.User.create(
            email=request.data['email'],
            name=request.data['name'],
            dob=request.data['dob'],
            pic=request.data['pic']
        )
        serializers.model.UserStats.create(email=user.email)
        return Response(self.serialize_user(user), status=status.HTTP_201_CREATED)

    def retrieve(self, request, email=None):
        user = get_object_or_404(serializers.model.User, email=email)
        if isinstance(user, serializers.model.User):
            return Response(self.serialize_user(user))
        return Response(user)


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

    def check_completion(self, *args, **kwargs):
        stats = None
        try:
            stats = serializers.model.UserStatsByMarathon.objects.filter(marathon_id=self.kwargs['marathon_id'], email=self.kwargs['email'])[0]
            stats = serializers.UserStatsByMarathonSerializer(stats).data
        except IndexError:
            stats = False
        if not stats:
            return Response(exception=Http404(), status=status.HTTP_404_NOT_FOUND)
        return Response(data=stats)