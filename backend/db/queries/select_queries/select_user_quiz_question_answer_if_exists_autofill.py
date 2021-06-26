# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_user_quiz_question_answer_if_exists_autofill_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz):
  localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_autofill_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_answers_master_table WHERE quiz_answer_slack_team_id=%s AND quiz_answer_slack_channel_id=%s AND quiz_answer_user_uuid_fk=%s AND quiz_answer_quiz_uuid_fk=%s", [slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_arr = postgres_cursor.fetchall()
    
    if result_arr == None or not result_arr or result_arr == []:
      localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_autofill_function END ===========================================')
      return None

    localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_autofill_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_autofill_function END ===========================================')
      return None