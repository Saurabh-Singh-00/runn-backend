from django_cassandra_engine.rest import serializers as cass_serializers
from rest_framework.fields import ListField
from .. import models as model


class CassandraSetField(ListField):

    def __init__(self, *args, **kwargs):
        self._type = args
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class CassandraTupleField(ListField):

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

    def validate_id(self, data):
        if data == "" or data == None:
            import uuid
            return uuid.uuid4()
        return data

    def validate_date_time(self, data):
        if data == "" or data == None:
            import datetime
            return datetime.datetime.now()
        return data

    def validate_sponsors(self, data):
        s = set()
        if data == None or isinstance(data, str):
            return None
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

    def validate_joined_at(self, data):
        if data == "" or data == None:
            import datetime
            return datetime.datetime.now()
        return data

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
