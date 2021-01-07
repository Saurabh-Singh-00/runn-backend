from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from . import serializers


class MarathonViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.MarathonSerializer

    def get_queryset(self):
        if self.kwargs == {} and self.request.GET == {}:
            return serializers.model.Marathon.objects.allow_filtering()
        return serializers.model.Marathon.objects.filter(**self.request.GET.dict())


class RunnerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.RunnerSerializer

    def get_queryset(self):
        return serializers.model.Runner.objects.filter(**self.kwargs)


class MarathonByRunnerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.MarathonByRunnerSerializer

    def get_queryset(self):
        return serializers.model.MarathonsByRunner.objects.filter(**self.kwargs)


class MarathonBySponsorViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = serializers.MarathonsBySponsorSerializer

    def get_queryset(self):
        return serializers.model.MarathonsBySponsor.objects.filter(**self.kwargs)
