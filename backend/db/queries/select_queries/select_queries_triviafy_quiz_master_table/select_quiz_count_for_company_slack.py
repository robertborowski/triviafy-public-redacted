# -------------------------------------------------------------- Imports
import psycopg2
from psycopg2 import Error
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def select_quiz_count_for_company_slack_function(postgres_connection, postgres_cursor, slack_workspace_team_id, slack_channel_id):
  localhost_print_function('=========================================== select_quiz_count_for_company_slack_function START ===========================================')
  
  try:
    # ------------------------ Query START ------------------------
    postgres_cursor.execute("SELECT COUNT(*) FROM triviafy_quiz_master_table WHERE quiz_slack_team_id=%s AND quiz_slack_channel_id=%s", [slack_workspace_team_id, slack_channel_id])
    # ------------------------ Query END ------------------------


    # ------------------------ Query Result START ------------------------
    result_row = postgres_cursor.fetchone()
    if result_row == None or result_row == []:
      localhost_print_function('=========================================== select_quiz_count_for_company_slack_function END ===========================================')
      return 0

    localhost_print_function('=========================================== select_quiz_count_for_company_slack_function END ===========================================')
    return result_row
    # ------------------------ Query Result END ------------------------
  
  
  except (Exception, psycopg2.Error) as error:
    if(postgres_connection):
      localhost_print_function('Except error hit: ', error)
      localhost_print_function('=========================================== select_quiz_count_for_company_slack_function END ===========================================')
      return 0