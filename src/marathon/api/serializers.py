from django_cassandra_engine.rest import serializers as cass_serializers
from rest_framework.fields import Field
from .. import models as model


class CassandraSetField(Field):

    def __init__(self, *args, **kwargs):
        self._type = args
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class CassandraTupleField(Field):

    def __init__(self, *args, **kwargs):
        self._type = args
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class MarathonSerializer(cass_serializers.DjangoCassandraModelSerializer):

    serializer_field_mapping = {
        **cass_serializers.DjangoCassandraModelSerializer.serializer_field_mapping,
        **{
            model.columns.Tuple: CassandraTupleField,
            model.columns.Set: CassandraSetField
        }
    }

    def validate_sponsors(self, data):
        s = set()
        if data == None:
            return data
        for sponsor in data:
            s.add(model.SponsorType(**sponsor))
        return s

    def validate_start_location(self, data):
        return tuple(data)

    def validate_end_location(self, data):
        return tuple(data)

    class Meta:
        model = model.Marathon
        fields = '__all__'


class RunnerSerializer(cass_serializers.DjangoCassandraModelSerializer):

    class Meta:
        model = model.Runner
        fields = '__all__'


class MarathonByRunnerSerializer(cass_serializers.DjangoCassandraModelSerializer):

    class Meta:
        model = model.MarathonsByRunner
        fields = '__all__'


class MarathonsBySponsorSerializer(cass_serializers.DjangoCassandraModelSerializer):

    class Meta:
        model = model.MarathonsBySponsor
        fields = '__all__'
