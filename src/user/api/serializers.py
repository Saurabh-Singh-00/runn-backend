from django_cassandra_engine.rest import serializers as cass_serializers
from rest_framework.serializers import DateTimeField, DateField
import datetime
from .. import models as model


class UserSerializer(cass_serializers.DjangoCassandraModelSerializer):

    dob = DateField(format=None)

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
            model.columns.DateTime: DateTimeField,
        }
    }

    def validate_time(self, data):
        if data == None or data == "":
            return datetime.datetime.now()
        return data

    class Meta:
        model = model.UserStatsByMarathon
        fields = '__all__'
