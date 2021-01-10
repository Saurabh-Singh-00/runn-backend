from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from . import serializers


class MarathonViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.MarathonSerializer

    def get_queryset(self):
        if self.kwargs == {} and self.request.GET == {}:
            return serializers.model.Marathon.objects.allow_filtering()
        return serializers.model.Marathon.objects.filter(**self.request.GET.dict())

    def create(self, request, *args, **kwargs):
        marathon = super().create(request, *args, **kwargs)
        data = marathon.data
        if data['sponsors'] != None and len(data['sponsors']) > 0:
            for sponsor in data['sponsors']:
                serializers.model.MarathonsBySponsor.create(
                    sponsor_id=sponsor['email'],
                    id=data['id'],
                    country=data['country'],
                    title=data['title'],
                    distance=data['distance']
                )        
        return marathon

    def retrieve(self, request, country, id):
        marathon = get_object_or_404(
            serializers.model.Marathon, country=country, id=id)
        return Response(serializers.MarathonSerializer(marathon).data)


class RunnerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.RunnerSerializer

    def get_queryset(self):
        return serializers.model.Runner.objects.filter(**self.kwargs)

    def create(self, request, marathon_id, *args, **kwargs):
        data = request.data
        marathon = get_object_or_404(
            serializers.model.Marathon, country=data['marathon_country'], id=data['marathon_id'])
        serializers.model.MarathonsByRunner.create(
            user_email=data['email'],
            country=data['marathon_country'],
            id=data['marathon_id'],
            title=marathon.title,
            distance=marathon.distance
        )
        return super().create(request, *args, **kwargs)


class MarathonByRunnerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.MarathonByRunnerSerializer

    def get_queryset(self):
        return serializers.model.MarathonsByRunner.objects.filter(**self.kwargs)


class MarathonBySponsorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.MarathonsBySponsorSerializer

    def get_queryset(self):
        return serializers.model.MarathonsBySponsor.objects.filter(**self.kwargs)
