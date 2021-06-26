# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_triviafy_quiz_answers_master_table_user_answer_function(postgres_connection, postgres_cursor, question_id, user_uuid):
  print('=========================================== select_triviafy_quiz_answers_master_table_user_answer_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT quiz_answer_quiz_question_uuid_fk, quiz_answer_actual_user_answer, quiz_answer_provided_is_correct FROM triviafy_quiz_answers_master_table WHERE quiz_answer_quiz_question_uuid_fk=%s AND quiz_answer_user_uuid_fk=%s", [question_id, user_uuid])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      print('returining None')
      print('=========================================== select_triviafy_quiz_answers_master_table_user_answer_function END ===========================================')
      return None
    

    print('=========================================== select_triviafy_quiz_answers_master_table_user_answer_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      print('=========================================== select_triviafy_quiz_answers_master_table_user_answer_function END ===========================================')
      return None