import psycopg2
from psycopg2 import Error
import os

def postgres_connect_to_database_function():
  print('=========================================== postgres_connect_to_database_function START ===========================================')

  # Heroku Postgres connection
  DATABASE_URL = os.environ.get('DATABASE_URL')
  postgres_connection = psycopg2.connect(DATABASE_URL, sslmode='require')

  postgres_cursor = postgres_connection.cursor()
  print('returning connection and cursor')
  print('=========================================== postgres_connect_to_database_function END ===========================================')
  return postgres_connection, postgres_cursor
  