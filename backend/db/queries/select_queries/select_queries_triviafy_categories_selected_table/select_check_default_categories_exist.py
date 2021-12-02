# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_check_default_categories_exist_function(postgres_connection, postgres_cursor, categories_team_id_fk, categories_channel_id_fk):
  localhost_print_function('=========================================== select_check_default_categories_exist_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_categories_selected_table WHERE categories_team_id_fk=%s AND categories_channel_id_fk=%s;", [categories_team_id_fk, categories_channel_id_fk])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_check_default_categories_exist_function END ===========================================')
      return None
    
    localhost_print_function('=========================================== select_check_default_categories_exist_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_check_default_categories_exist_function END ===========================================')
      return None