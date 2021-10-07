# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def delete_query_delete_skipped_quiz_function(postgres_connection, postgres_cursor, quiz_uuid):
  localhost_print_function('=========================================== delete_query_delete_skipped_quiz_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("DELETE FROM triviafy_quiz_master_table WHERE uuid_quiz=%s", [quiz_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    postgres_connection.commit()
    localhost_print_function('=========================================== delete_query_delete_skipped_quiz_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== delete_query_delete_skipped_quiz_function END ===========================================')
      return None