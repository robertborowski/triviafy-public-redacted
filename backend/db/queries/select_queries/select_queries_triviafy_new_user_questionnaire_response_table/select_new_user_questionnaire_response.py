# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_new_user_questionnaire_response_function(postgres_connection, postgres_cursor, user_slack_uuid, user_slack_team_id, user_slack_channel_id):
  localhost_print_function('=========================================== select_new_user_questionnaire_response_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT * FROM triviafy_new_user_questionnaire_response_table WHERE questionnaire_user_slack_uuid_fk=%s AND questionnaire_user_slack_team_id_fk=%s AND questionnaire_user_slack_channel_id_fk=%s", [user_slack_uuid, user_slack_team_id, user_slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_new_user_questionnaire_response_function END ===========================================')
      return None
    
    localhost_print_function('=========================================== select_new_user_questionnaire_response_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_new_user_questionnaire_response_function END ===========================================')
      return None