import psycopg2
from psycopg2 import Error
import os

def connect_to_postgres_function():
  """Returns: Postgres Connection and cursor"""
  
  # Heroku Postgres connection
  DATABASE_URL = os.environ.get('TRIVIAFY_DATABASE_URL')
  connection_postgres = psycopg2.connect(DATABASE_URL, sslmode='require')
  

  cursor = connection_postgres.cursor()
  return connection_postgres, cursor