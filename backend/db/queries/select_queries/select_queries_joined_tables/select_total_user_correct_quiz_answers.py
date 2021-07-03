# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_total_user_correct_quiz_answers_function(postgres_connection, postgres_cursor, user_uuid, company_latest_quiz_id):
  localhost_print_function('=========================================== select_total_user_correct_quiz_answers_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT COUNT(answers.*)FROM triviafy_quiz_answers_master_table AS answers LEFT JOIN triviafy_user_login_information_table_slack AS users ON answers.quiz_answer_user_uuid_fk=users.user_uuid WHERE answers.quiz_answer_provided_is_correct=TRUE AND answers.quiz_answer_user_uuid_fk=%s AND answers.quiz_answer_quiz_uuid_fk<>%s", [user_uuid, company_latest_quiz_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_total_user_correct_quiz_answers_function END ===========================================')
      return 0
    
    localhost_print_function('=========================================== select_total_user_correct_quiz_answers_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_total_user_correct_quiz_answers_function END ===========================================')
      return result_row