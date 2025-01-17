"""
This type stub file was generated by pyright.
"""

__all__ = ["DEFAULT_CONNECTION_NAME", "DEFAULT_DATABASE_NAME", "ConnectionFailure", "connect", "disconnect", "disconnect_all", "get_connection", "get_db", "register_connection"]
DEFAULT_CONNECTION_NAME = ...
DEFAULT_DATABASE_NAME = ...
DEFAULT_HOST = ...
DEFAULT_PORT = ...
_connection_settings = ...
_connections = ...
_dbs = ...
READ_PREFERENCE = ...
class ConnectionFailure(Exception):
    """Error raised when the database connection can't be established or
    when a connection with a requested alias can't be retrieved.
    """
    ...


def register_connection(alias, db=..., name=..., host=..., port=..., read_preference=..., username=..., password=..., authentication_source=..., authentication_mechanism=..., authmechanismproperties=..., **kwargs): # -> None:
    """Register the connection settings.

    :param alias: the name that will be used to refer to this connection throughout MongoEngine
    :param db: the name of the database to use, for compatibility with connect
    :param name: the name of the specific database to use
    :param host: the host name of the: program: `mongod` instance to connect to
    :param port: the port that the: program: `mongod` instance is running on
    :param read_preference: The read preference for the collection
    :param username: username to authenticate with
    :param password: password to authenticate with
    :param authentication_source: database to authenticate against
    :param authentication_mechanism: database authentication mechanisms.
        By default, use SCRAM-SHA-1 with MongoDB 3.0 and later,
        MONGODB-CR (MongoDB Challenge Response protocol) for older servers.
    :param mongo_client_class: using alternative connection client other than
        pymongo.MongoClient, e.g. mongomock, montydb, that provides pymongo alike
        interface but not necessarily for connecting to a real mongo instance.
    :param kwargs: ad-hoc parameters to be passed into the pymongo driver,
        for example maxpoolsize, tz_aware, etc. See the documentation
        for pymongo's `MongoClient` for a full list.
    """
    ...

def disconnect(alias=...): # -> None:
    """Close the connection with a given alias."""
    ...

def disconnect_all(): # -> None:
    """Close all registered database."""
    ...

def get_connection(alias=..., reconnect=...):
    """Return a connection with a given alias."""
    ...

def get_db(alias=..., reconnect=...):
    ...

def connect(db=..., alias=..., **kwargs):
    """Connect to the database specified by the 'db' argument.

    Connection settings may be provided here as well if the database is not
    running on the default port on localhost. If authentication is needed,
    provide username and password arguments as well.

    Multiple databases are supported by using aliases. Provide a separate
    `alias` to connect to a different instance of: program: `mongod`.

    In order to replace a connection identified by a given alias, you'll
    need to call ``disconnect`` first

    See the docstring for `register_connection` for more details about all
    supported kwargs.
    """
    ...

_get_connection = ...
_get_db = ...
