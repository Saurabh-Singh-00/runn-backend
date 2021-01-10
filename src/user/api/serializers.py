from django_cassandra_engine.rest import serializers as cass_serializers
from rest_framework.serializers import DateTimeField
import datetime
from .. import models as model

class CassandraTimeField(DateTimeField):

    def __init__(self, *args, **kwargs):
        self._type = args
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data

class UserSerializer(cass_serializers.DjangoCassandraModelSerializer):

    class Meta:
        model = model.User
        fields = '__all__'


class UserStatsSerializer(cass_serializers.DjangoCassandraModelSerializer):

    class Meta:
        model = model.UserStats
        fields = '__all__'


class UserStatsByMarathonSerializer(cass_serializers.DjangoCassandraModelSerializer):

    serializer_field_mapping = {
        **cass_serializers.DjangoCassandraModelSerializer.serializer_field_mapping,
        **{
            model.columns.DateTime: CassandraTimeField,
        }
    }

    def validate_time(self, data):
        if data == None or data == "":
            return datetime.datetime.now()

    class Meta:
        model = model.UserStatsByMarathon
        fields = '__all__'
