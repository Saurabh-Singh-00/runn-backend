from cassandra.cqlengine.models import columns
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine.usertype import UserType
from django.db import connections
from cassandra.cluster import UserTypeDoesNotExist
import os
import uuid
import datetime

setattr(columns.Column, 'verbose_name', None)

class SponsorType(UserType):

    email = columns.Text()
    name = columns.Text()
    logo = columns.Text()

    def validate(self):
        return self

    def __hash__(self):
        return hash((self.email))


user_types = [SponsorType]
database_name = 'runn'
keyspace = os.getenv('CASSANDRA_KEYSPACE')
connection = connections['cassandra']

for udt in user_types:
    try:
        connection.connection.cluster.register_user_type(
            keyspace, udt.type_name(), udt)
    except UserTypeDoesNotExist as e:
        print(e)


class Marathon(DjangoCassandraModel):
    """
    Marathon Database Object
    """
    __table_name__ = 'marathon'
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    country = columns.Text(partition_key=True)
    id = columns.UUID(primary_key=True, default=uuid.uuid4,
                      clustering_order='ASC')
    state = columns.Text()
    city = columns.Text()
    pincode = columns.Integer()
    date_time = columns.DateTime(default=datetime.datetime.now())
    title = columns.Text()
    description = columns.Text()
    organiser_email = columns.Text()
    start_location = columns.Tuple(columns.Float, columns.Float)
    columns.BaseCollectionColumn._freeze_db_type(start_location)
    end_location = columns.Tuple(columns.Float, columns.Float)
    columns.BaseCollectionColumn._freeze_db_type(end_location)
    distance = columns.Float()
    type = columns.Text()
    sponsors = columns.Set(columns.UserDefinedType(SponsorType))

    class Meta:
        get_pk_field = 'country'
        app_label = 'marathon'


class Runner(DjangoCassandraModel):
    """
    Runner Database Object
    """
    __table_name__ = 'runner'
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    marathon_id = columns.UUID(partition_key=True)
    marathon_country = columns.Text(primary_key=True)
    email = columns.Text(primary_key=True, clustering_order='ASC')
    name = columns.Text()
    pic = columns.Text()
    participation_type = columns.Text()
    joined_at = columns.DateTime(default=datetime.datetime.now())

    class Meta:
        get_pk_field = 'marathon_id'
        app_label = 'marathon'


class MarathonsByRunner(DjangoCassandraModel):
    """
    MarathonsByRunner Database Object
    """
    __table_name__ = 'marathons_by_runner'
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    user_email = columns.Text(partition_key=True)
    country = columns.Text(primary_key=True)
    id = columns.UUID(primary_key=True, clustering_order='ASC')
    title = columns.Text()
    distance = columns.Float()

    class Meta:
        get_pk_field = 'user_email'
        app_label = 'marathon'


class MarathonsBySponsor(DjangoCassandraModel):
    """
    MarathonsBySponsor Database Object
    """
    __table_name__ = 'marathons_by_sponsor'
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    sponsor_id = columns.Text(partition_key=True)
    id = columns.UUID(primary_key=True)
    country = columns.Text(primary_key=True)
    title = columns.Text()
    distance = columns.Float()

    class Meta:
        get_pk_field = 'sponsor_id'
        app_label = 'marathon'
