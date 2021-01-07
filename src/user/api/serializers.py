from django_cassandra_engine.rest import serializers as cass_serializers
from rest_framework.serializers import DateField
from .. import models as model


class UserSerializer(cass_serializers.DjangoCassandraModelSerializer):

    class Meta:
        model = model.User
        fields = '__all__'


class UserStatsSerializer(cass_serializers.DjangoCassandraModelSerializer):

    class Meta:
        model = model.UserStats
        fields = '__all__'
