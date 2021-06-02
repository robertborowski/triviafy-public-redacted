import psycopg2
from psycopg2 import Error

def postgres_close_connection_to_database_function(postgres_connection, postgres_cursor):
  print('=========================================== postgres_close_connection_to_database_function START ===========================================')
  postgres_cursor.close()
  postgres_connection.close()
  print('closing the database connection and cursor')
  print('=========================================== postgres_close_connection_to_database_function END ===========================================')