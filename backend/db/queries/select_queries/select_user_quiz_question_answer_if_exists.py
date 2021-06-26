# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_user_quiz_question_answer_if_exists_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz, question_uuid_k):
  localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_quiz_answers_master_table WHERE quiz_answer_slack_team_id=%s AND quiz_answer_slack_channel_id=%s AND quiz_answer_user_uuid_fk=%s AND quiz_answer_quiz_uuid_fk=%s AND quiz_answer_quiz_question_uuid_fk=%s", [slack_workspace_team_id, slack_channel_id, user_uuid, uuid_quiz, question_uuid_k])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_function END ===========================================')
      return None, None
    
    localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_function END ===========================================')
    return result_row[0], result_row[7]
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_user_quiz_question_answer_if_exists_function END ===========================================')
      return None, None