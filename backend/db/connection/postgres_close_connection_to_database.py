import psycopg2
from psycopg2 import Error

def postgres_close_connection_to_database_function(postgres_connection, postgres_cursor):
  """Returns: Closes the connections to postgres"""
  postgres_cursor.close()
  postgres_connection.close()