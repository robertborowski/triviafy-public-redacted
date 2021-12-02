# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def insert_category_table_function(postgres_connection, postgres_cursor, categories_uuid_pk, categories_timestamp, categories_team_id_fk, categories_channel_id_fk, categories_selected):
  localhost_print_function('=========================================== insert_category_table_function START ===========================================')
  
  # ------------------------ Query START ------------------------
  postgres_insert_query = """INSERT INTO triviafy_categories_selected_table(categories_uuid_pk,categories_timestamp,categories_team_id_fk,categories_channel_id_fk,categories_selected) VALUES(%s,%s,%s,%s,%s);"""
  # ------------------------ Query END ------------------------


  # ------------------------ Record row START ------------------------
  record_to_insert = (categories_uuid_pk, categories_timestamp, categories_team_id_fk, categories_channel_id_fk, categories_selected)
  # ------------------------ Record row END ------------------------


  # ------------------------ Insert attempt START ------------------------
  try:
    postgres_cursor.execute(postgres_insert_query, record_to_insert)
    postgres_connection.commit()
    
    localhost_print_function('=========================================== insert_category_table_function END ===========================================')
    return True
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== insert_category_table_function END ===========================================')
      return False
  # ------------------------ Insert attempt END ------------------------