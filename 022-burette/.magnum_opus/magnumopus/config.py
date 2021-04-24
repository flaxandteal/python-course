import os
from cassandra.auth import PlainTextAuthProvider

class Config:
    CASSANDRA_HOSTS = os.environ.get('CASSANDRA_HOSTS', 'cassandra').split()
    CASSANDRA_KEYSPACE = os.environ.get('CASSANDRA_KEYSPACE', 'pythoncourse')
    CASSANDRA_SETUP_KWARGS = {
        'protocol_version': 3,
        'port': os.environ.get('CASSANDRA_PORT', 9042),
        'auth_provider': PlainTextAuthProvider(
            username='cassandra',
            password=os.environ.get('CASSANDRA_PASSWORD')
        )
    }
    PANTRY_STORE = os.environ.get('MAGNUMOPUS_PANTRY_STORE', 'cqlalchemy')
