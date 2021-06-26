# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_question_ids_already_asked_to_company_slack_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id):
  localhost_print_function('=========================================== select_question_ids_already_asked_to_company_slack_function START ===========================================')

  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT quiz_question_asked_tracking_question_uuid FROM triviafy_quiz_questions_asked_to_company_slack_table WHERE quiz_question_asked_tracking_slack_team_id=%s AND quiz_question_asked_tracking_slack_channel_id=%s", [slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    # Get the results arr
    result_arr = postgres_cursor.fetchall()
    if result_arr == None or result_arr == []:
      localhost_print_function('=========================================== select_question_ids_already_asked_to_company_slack_function END ===========================================')
      return None

    localhost_print_function('=========================================== select_question_ids_already_asked_to_company_slack_function END ===========================================')  
    return result_arr
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_question_ids_already_asked_to_company_slack_function END ===========================================')
      return result_arr