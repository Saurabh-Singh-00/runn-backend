from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns
import os
import datetime

setattr(columns.Column, 'verbose_name', None)

class User(DjangoCassandraModel):
    """
    User Database Object
    """
    __table_name__ = "user"
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    email = columns.Text(partition_key=True)
    name = columns.Text()
    pic = columns.Text()
    dob = columns.Date()

    class Meta:
        get_pk_field = 'email'
        app_label = 'user'


class Sponsor(DjangoCassandraModel):
    """
    Sponsor Database Object
    """
    __table_name__ = "sponsor"
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    email = columns.Text(partition_key=True)
    name = columns.Text(primary_key=True)
    logo = columns.Text()
    website = columns.Text()
    description = columns.Text()

    class Meta:
        get_pk_field = 'email'
        app_label = 'user'


class UserStats(DjangoCassandraModel):
    """
    UserStats Database Object
    """
    __table_name__ = "user_stats"
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    email = columns.Text(partition_key=True)
    steps = columns.Counter()
    distance = columns.Counter()

    class Meta:
        get_pk_field = 'email'
        app_label = 'user'


class UserStatsByMarathon(DjangoCassandraModel):
    """
    UserStatsByMarathon Database Object
    """
    __table_name__ = 'user_stats_by_marathon'
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')

    marathon_id = columns.UUID(partition_key=True)
    email = columns.Text(partition_key=True)
    time = columns.DateTime(primary_key=True, default=datetime.datetime.now())
    lat = columns.Float()
    long = columns.Float()

    class Meta:
        get_pk_field = 'marathon_id'
        app_label = 'user'