# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_one_user_incoming_webhook_function(postgres_connection, postgres_cursor, quiz_slack_team_id, quiz_slack_channel_id):
  localhost_print_function('=========================================== select_one_user_incoming_webhook_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT user_slack_team_channel_incoming_webhook_url FROM triviafy_user_login_information_table_slack WHERE user_slack_workspace_team_id=%s AND user_slack_channel_id=%s ORDER BY user_datetime_account_created ASC;", [quiz_slack_team_id, quiz_slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_one_user_incoming_webhook_function END ===========================================')
      return None
    
    localhost_print_function('=========================================== select_one_user_incoming_webhook_function END ===========================================')
    return result_row[0]
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_one_user_incoming_webhook_function END ===========================================')
      return None