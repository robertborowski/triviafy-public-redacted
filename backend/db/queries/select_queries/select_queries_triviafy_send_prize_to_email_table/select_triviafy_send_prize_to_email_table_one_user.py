# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_triviafy_send_prize_to_email_table_one_user_function(postgres_connection, postgres_cursor, user_uuid):
  localhost_print_function('=========================================== select_triviafy_send_prize_to_email_table_one_user_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_send_prize_to_email_table WHERE send_prize_to_user_uuid_fk=%s", [user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_triviafy_send_prize_to_email_table_one_user_function END ===========================================')
      return None
    
    localhost_print_function('=========================================== select_triviafy_send_prize_to_email_table_one_user_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_triviafy_send_prize_to_email_table_one_user_function END ===========================================')
      return None