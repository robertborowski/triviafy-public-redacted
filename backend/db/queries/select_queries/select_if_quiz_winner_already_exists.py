# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_if_quiz_winner_already_exists_function(postgres_connection, postgres_cursor, uuid_quiz, winner_user_uuid):
  localhost_print_function('=========================================== select_if_quiz_winner_already_exists_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_winners_table WHERE quiz_winner_quiz_uuid_fk=%s AND quiz_winner_user_uuid_fk=%s", [uuid_quiz, winner_user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_if_quiz_winner_already_exists_function END ===========================================')
      return False
    
    localhost_print_function('=========================================== select_if_quiz_winner_already_exists_function END ===========================================')
    return True
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_if_quiz_winner_already_exists_function END ===========================================')
      return False