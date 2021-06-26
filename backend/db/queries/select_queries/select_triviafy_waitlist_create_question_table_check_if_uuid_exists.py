# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function(postgres_connection, postgres_cursor, user_uuid):
  localhost_print_function('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function START ===========================================')
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_waitlist_create_question_table WHERE waitlist_user_uuid_signed_up=%s", [user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function END ===========================================')
      return None
    
    localhost_print_function('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_triviafy_waitlist_create_question_table_check_if_uuid_exists_function END ===========================================')
      return None